#Open the data file.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}


#election_data = open(file_to_load, "r")

with open(file_to_load) as election_data:

# Create a filename variable to a direct or indirect path to the file.
# Using the open() function with the "w" mode we will write data to the file.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    #open(file_to_save, "w")

    # Print the file object.
    #print(election_data)
#Write down the names of all the candidates.
    # Print the candidate list.
        
    # Read and print the header row.
    #print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes =+ 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            print(candidate_options)
#Add a vote count for each candidate.
           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0


        candidate_votes[candidate_name] += 1

#Get the total votes for each candidate.


#Get the total votes cast for the election.
    print(candidate_votes)

# Close the file.



# Create a filename variable to a direct or indirect path to the file.


# Using the with statement open the file as a text file.




