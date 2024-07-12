from scripts.parse_data import process_data
import json

def main():

    file_path = 'data/oomc_full.csv'
    weights = process_data(file_path)

    with open('parsed_data.json', 'w') as f:
        json.dump(weights, f, indent=4)

    # process_data(file_path)
    
    #TODO: Flatten JSON and read/write to a csv file for easier reading and manipulation.

if __name__ == '__main__':
    main()
