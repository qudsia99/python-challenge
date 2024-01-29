import os
import csv

# Initialize variables
candidate_dict = {}  # Dictionary to store candidate information
totalvotes = 0  # Total number of votes cast

# Create data file path
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# Opening file using 'r', as we are only extracting info.
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping header
    csvheader = next(csvreader)

    # Running for loop
    for row in csvreader:
        totalvotes += 1
        current_candidate = row[2]

        # Update candidate_dict
        if current_candidate not in candidate_dict:
            candidate_dict[current_candidate] = 1
        else:
            candidate_dict[current_candidate] += 1

# Find the winner
winner = max(candidate_dict, key=candidate_dict.get)

# Calculate the percentage of votes each candidate won
percentage_votes = {candidate: (votes / totalvotes) * 100 for candidate, votes in candidate_dict.items()}

# Display results
print(f"Total Votes Cast: {totalvotes}")
print("List of Candidates:")
for candidate in candidate_dict:
    print(f"{candidate}: {candidate_dict[candidate]} votes ({percentage_votes[candidate]:.2f}%)")
print(f"Winner: {winner} with {candidate_dict[winner]} votes ({percentage_votes[winner]:.2f}%)")

# Now to export our cleaned data to a new file.
poll_cleaned = os.path.join("PyPoll", "Analysis", "pollclean.csv")

# Open file with writing ability
with open(poll_cleaned, 'w', newline="") as pollfile:
    csvwriter = csv.writer(pollfile)

    # Create header
    csvwriter.writerow(["Total Votes Cast", "List of Candidates", "Total Votes Per Candidate", "Percentage of Votes", "Winner"])

    # Filling in row values, using dictionary
    for candidate, votes in candidate_dict.items():
        csvwriter.writerow([totalvotes, candidate, votes, round(percentage_votes[candidate],3), winner])