# Add our dependencies.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Get the candidate names by delcaring a new list
candidate_options = []

# Declare an empty dictionary for each candidates votes
candidate_votes = {}

# Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:   
    file_reader = csv.reader(election_data)

# Read the header row.
    headers = next(file_reader)
  
# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Count each time a candidate name appears 
        candidate_votes[candidate_name] += 1   

    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")



        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes 
            winning_percentage = vote_percentage     
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)   









# 1. Total number of votes cast
# 2. Complete list of the candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote


# Close the file.
