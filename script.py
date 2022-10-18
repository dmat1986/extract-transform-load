"""
An input CSV file containing statistical information about diseases in different locations is given.

Here are the definitions of each column in the input file:

1. location_code: The unique identifier of the location
2. disease: Name of the disease
3. prevalence: Number of people having the disease
4. population: Number of people living in the location

Please complete the following Python function that:
(a) calculates the percentage of people who have each disease in each location, and
(b) writes the result to a specified CSV file

Notes:
1. If there is no information about a disease for a specific location, the percentage should be considered zero.
2. The output file should contain a column specifying the location and a column for each disease.
3. The samples of input and output files have been attached.
"""

import sys
import pandas as pd

def calculate_prevalence_rate_by_location(input_path: str, output_path: str) -> None:
    #Read the data from the csv file
    dataset = pd.read_csv(input_path)

    #Find the percentage of people who have each disease in each location
    #and round to 2 decimal places
    dataset["percentage"] = (dataset["prevalence"]/dataset["population"])*100
    dataset["percentage"] = dataset["percentage"].astype(float).round(2)

    #Group the data
    percent_by_loc = dataset.groupby(["location_code","disease"])["percentage"].sum()
    percent_by_loc = pd.DataFrame(percent_by_loc)

    #Pivot the table so that each disease is a column heading
    percent_by_loc = percent_by_loc.pivot_table('percentage', ['location_code'], 'disease').fillna(0)

    #Write to csv
    f = open(output_path, 'w')
    percent_by_loc.to_csv(f)



if __name__ == '__main__':
    input_path = str(sys.argv[1]).strip()
    output_path = str(sys.argv[2]).strip()

    calculate_prevalence_rate_by_location(input_path, output_path)
