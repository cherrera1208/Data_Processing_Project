# Data Processing and Analysis Tool

## Overview
This project is a tool for processing and analyzing large datasets from CSV files. It reads data, assigns weights, and performs basic analysis to count occurrences and instances.

## Features
- Efficient data processing for large datasets using chunk processing
- Basic data analysis and occurrence counting
- Data normalization to ensure accurate weighted totals
- Modular design for easy extension and maintenance
- JSON output for parsed data, term frequencies, and aggregated categories

## Tools Used
 - Python
 - WSL Terminal
 - Pandas
 - NumPy
 - NLTK
 - git (github, git large file storage)

## Installation and Usage
```
python3 main.py
```
To run the aggregator function:
```
cd scripts
python3 agg.py
```
## Thought Process and Development Journey
### Initial Concept

- The initial concept for this project was to create a tool that could efficiently process and analyze large datasets from CSV files. The goal was to read the data, assign weights, and perform basic analysis to count occurrences and instances.
Challenges and Solutions

### Challenge 1: Efficient Data Reading

  - Solution: Implemented optimized data reading techniquesto handle large datasets without excessive memory usage.Standard Python libraries such as Pandas, NumPy, and NLTKwere used to achieve this.

  - Specifically, pandas chunk DataFrames to process data in1000 chunk sized batches to reduce memory usage. My PCcould not run the script without this implementation.

### Challenge 2: Data Normalization

  - Solution: Normalized the data using a standard- normalization equation to ensure accurate weighted totals- that precisely represent the data.

### Final Implementation

The program runs from a single main.py command in the terminal and produces three files from the initial raw data:

  - parsed_data.json: Contains the processed data with weights.
  - term_freq.json: Contains the most common words and their frequencies.
  - aggregated_data.json: Aggregates categories to eliminate redundancies.

### Further Goals

The project could be improved with:

  - Clean, refactored code
  - Effective testing and error handling
  - Refactor agg.py script to accept the parsed_data.json file and aggregate based on base categories of json, as it is now, it can only read a hardcoded dictionary of data. This is not useful as is
  - Utilize the aggregated data to more refine the results
  - Visualization of the data in a dashboard using Django or a similar library
