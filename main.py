from scripts.parse_data import process_data
from scripts.term_freq import word_freq


def main():
    file_path = 'data/oomc_full.csv'

    process_data(file_path)
    print(word_freq)

    #TODO: Flatten JSON and read/write to a csv file for easier reading and manipulation.

if __name__ == '__main__':
    main()
