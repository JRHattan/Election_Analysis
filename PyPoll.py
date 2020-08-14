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
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
                
        

#Get the total votes for each candidate.
    

#Get the total votes cast for the election.

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Close the file.
election_data.close()


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)