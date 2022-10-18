The input is CSV file containing statistical information about diseases in different locations.

The definitions of each column in the input file:

1. location_code: The unique identifier of the location
2. disease: Name of the disease
3. prevalence: Number of people having the disease
4. population: Number of people living in the location

This script:

(a) calculates the percentage of people who have each disease in each location, and
(b) writes the result to a specified CSV file

Notes:
1. If there is no information about a disease for a specific location, the percentage is considered zero.
2. The output file contains a column specifying the location and a column for each disease.
