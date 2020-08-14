#Open the data file.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#election_data = open(file_to_load, "r")

with open(file_to_load) as election_data:

# Create a filename variable to a direct or indirect path to the file.
# Using the open() function with the "w" mode we will write data to the file.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    #open(file_to_save, "w")

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
#Add a vote count for each candidate.
           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
# 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
# 3. Calculate the percentage of votes.
        vote_percentage = round(float(votes) / float(total_votes) * 100, 2)

# 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        

#Get the total votes for each candidate.
    

#Get the total votes cast for the election.
print(total_votes)
print(winning_candidate)
# Close the file.



# Create a filename variable to a direct or indirect path to the file.


# Using the with statement open the file as a text file.




