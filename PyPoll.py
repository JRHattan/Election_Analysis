#Open the data file.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

election_data = open(file_to_load, "r")

with open(file_to_load) as election_data:

# Create a filename variable to a direct or indirect path to the file.
# Using the open() function with the "w" mode we will write data to the file.
    #open(file_to_save, "w")

    # Print the file object.
    #print(election_data)

#Write down the names of all the candidates.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
#Add a vote count for each candidate.


#Get the total votes for each candidate.


#Get the total votes cast for the election.

# Close the file.



# Create a filename variable to a direct or indirect path to the file.


# Using the with statement open the file as a text file.




