import pandas as pd
import json
from collections import defaultdict
from tqdm import tqdm

# Establishes the primary categories and their counts processed by defined panda chunk sizes
def process_chunk(chunk, counters):    
    for race, class_, inventory in zip(chunk['race'], chunk['class'], chunk['inventory']):
        counters['race_counter'][race] += 1
        counters['class_counter'][class_] += 1
        counters['race_class_counter'][race][class_] += 1

        # Establishes the secondary categories and their counts
        if isinstance(inventory, str):
            for item in inventory.split(','):
                counters['inventory_counter'][item] += 1
                counters['race_class_inventory_counter'][race][class_][item] += 1
                counters['race_inventory_counter'][race][item] += 1
                counters['class_inventory_counter'][class_][item] += 1

# Defines the formula to calculate the weights of different categories based on their counts
def calculate_percentage(counter, total):
    return {key: count / total for key, count in counter.items()}

# Calculates the weights with the formula above
def calculate_weights(counters, total_records):
    race_weights = calculate_percentage(counters['race_counter'], total_records)
    class_weights = calculate_percentage(counters['class_counter'], total_records)
    inventory_weights = calculate_percentage(counters['inventory_counter'], sum(counters['inventory_counter'].values()))

    total_race_class_counts = {race: sum(inner_dict.values()) for race, inner_dict in counters['race_class_counter'].items()}
    race_class_weights = {race: calculate_percentage(inner_dict, total_race_class_counts[race]) for race, inner_dict in counters['race_class_counter'].items()}

    total_race_inventory_counts = {race: sum(inner_dict.values()) for race, inner_dict in counters['race_inventory_counter'].items()}
    race_inventory_weights = {race: calculate_percentage(inner_dict, total_race_inventory_counts[race]) for race, inner_dict in counters['race_inventory_counter'].items()}

    total_class_inventory_counts = {class_: sum(inner_dict.values()) for class_, inner_dict in counters['class_inventory_counter'].items()}
    class_inventory_weights = {class_: calculate_percentage(inner_dict, total_class_inventory_counts[class_]) for class_, inner_dict in counters['class_inventory_counter'].items()}

    total_race_class_inventory_counts = {
        race: {
            class_: sum(inner_dict.values())
            for class_, inner_dict in counters['race_class_inventory_counter'][race].items()
        } for race in counters['race_class_inventory_counter']
    }
    race_class_inventory_weights = {
        race: {
            class_: calculate_percentage(inner_dict, total_race_class_inventory_counts[race][class_])
            for class_, inner_dict in counters['race_class_inventory_counter'][race].items()
        } for race in counters['race_class_inventory_counter']
    }

    return {
        'race_weights': race_weights,
        'class_weights': class_weights,
        'inventory_weights': inventory_weights,
        'race_class_weights': race_class_weights,
        'race_inventory_weights': race_inventory_weights,
        'class_inventory_weights': class_inventory_weights,
        'race_class_inventory_weights': race_class_inventory_weights,
    }

# Reads file_path in chunks because 1 million records is too large to read all at once
def process_data(file_path, chunksize=1000):
    total_rows = sum(1 for _ in open(file_path, encoding='utf-8')) - 1
    total_chunks = (total_rows // chunksize) + 1
    data = pd.read_csv(file_path, chunksize=chunksize)

    counters = {
        'race_counter': defaultdict(int),
        'class_counter': defaultdict(int),
        'race_class_counter': defaultdict(lambda: defaultdict(int)),
        'inventory_counter': defaultdict(int),
        'race_class_inventory_counter': defaultdict(lambda: defaultdict(lambda: defaultdict(int))),
        'race_inventory_counter': defaultdict(lambda: defaultdict(int)),
        'class_inventory_counter': defaultdict(lambda: defaultdict(int)),
    }

    total_records = 0

    for chunk in tqdm(data, desc='Processing data in chunks of 1000', unit="chunks", total=total_chunks, ncols=100, bar_format='{desc}: {percentage:3.0f}% |{bar}| {n_fmt}/{total_fmt} {postfix}'):
        process_chunk(chunk, counters)
        total_records += len(chunk)

    weights = calculate_weights(counters, total_records)

    print(f'Sum of class wights: {sum(weights["class_weights"].values())}')

    return weights
