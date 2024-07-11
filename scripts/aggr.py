import json

# Aggregates the data by common word and prints the sum of the aggregated values (to equal 1)
# This remove instances of subtypes like "Aasimar", "Aasimar (Dragon Child)", "Aasimar (Volo's Guide to Monsters)" top just "Aasimar"
# TODO: Only harcoded for now, but should be read from the "parsed_data.json" file
data = {
# Sample data from parsed_data.json, will cause the sum script to return < 1 as it is incomplete data, but it does work correctly
"Aarakocra": 0.027775075674778698,
        "Aasimar": 0.035432199785230496,
        "Aasimar (Dragon Child)": 1.9073668228800095e-06,
        "Aasimar (Volo's Guide to Monsters)": 1.9073668228800095e-06,
        "Abomination": 9.536834114400048e-07,
        "Abyssal Cambion ": 3.814733645760019e-06,
        "Ackrylil": 1.9073668228800095e-06,
        "Aeolan": 1.9073668228800095e-06,
        "Ailead": 1.9073668228800095e-06,
        "Ailthizar (Aasimar)": 1.0490517525840051e-05,
        "Air Genasi": 2.0981035051680103e-05,
        "Ajatar": 3.814733645760019e-06,
        "Alakar": 3.814733645760019e-06,
        "Amazon": 7.629467291520038e-06,
        "Amazonian": 2.8610502343200143e-06,
        "Amonkhet Minotaur": 4.768417057200024e-06,
        "Angel of Death": 9.536834114400048e-07,
        "Angelic Phoenix": 1.9073668228800095e-06,
        "Animated Armor": 1.9073668228800095e-06,
        "Anka": 9.536834114400048e-07,
        "Ann\u00fclian": 3.814733645760019e-06,
        "Anodod": 9.536834114400048e-07,
        "Anthropomorph": 1.9073668228800095e-06,
        "Anubite": 4.768417057200024e-06,
        "Ape": 9.536834114400048e-07,
        "Aquari": 6.675783880080033e-06,
        "Arachni": 1.2397884348720061e-05,
        "Aranthi (GnG)": 4.768417057200024e-06,
        "Arenea": 3.814733645760019e-06,
        "Aroura (Ratfolk)": 1.9073668228800095e-06,
        "Ashborn (AotG)": 9.536834114400048e-07,
        "Ashera": 5.7221004686400285e-06,
        "Asmodean Devil": 1.9073668228800095e-06,
        "Astral Elf": 1.3351567760160067e-05,
        "Atlantic Peoples": 4.768417057200024e-06,
        "Attalwen": 1.9073668228800095e-06,
        "Atuin": 1.9073668228800095e-06,
        "Auricar": 9.536834114400048e-07,
        "Autumn Hamadryad": 3.814733645760019e-06,
        "Avali": 1.9073668228800095e-06,
        "Avariel": 2.8610502343200143e-06,
        "Avatar": 9.536834114400048e-07,
        "Aven": 3.814733645760019e-06,
        "Awakened Animal": 1.9073668228800095e-06,
        "Awakened Beast": 1.9073668228800095e-06,
        "Awakened Cat": 1.0490517525840051e-05,
        "Awakened Dog": 1.9073668228800095e-06,
        "Awakened Flesh Golem": 4.768417057200024e-06,
        "Awakened fox": 9.536834114400048e-07,
        "Awakened Half-Dragon": 9.536834114400048e-07,
        "Awakened Tree": 9.536834114400048e-07,
        "Awakened Undead": 3.7193653046160186e-05,
        "Awoken Rabbit": 1.9073668228800095e-06,
        "Aynerth Minotaur": 9.536834114400048e-07,
        "Azlanti Pureblood": 2.8610502343200143e-06,
        "B\u00f8rn af fortiden": 9.536834114400048e-07,
        "B\u00f8rn af guderne": 1.9073668228800095e-06,
        "Badgerfolk": 3.814733645760019e-06,
        "Bag of Holding": 9.536834114400048e-07,
        "Baketako": 9.536834114400048e-07,
        "Bathynomian": 1.9073668228800095e-06,
        "Bearfolk": 1.9073668228800095e-06,
        "Bearkin": 2.574945210888013e-05,
        "Bearkin ": 1.9073668228800095e-06,
}

aggregated_data = {}

for key, value in data.items():
    base_category = key.split(" ")[0]

    # If the base category is already in the new dictionary, add the value to it
    if base_category in aggregated_data:
        aggregated_data[base_category] += value
    else:
        # If the base category is not in the new dictionary, add it
        aggregated_data[base_category] = value

with open('aggregated_data.json', 'w') as f:
    json.dump(aggregated_data, f, indent=4)

print(sum(aggregated_data.values()))
