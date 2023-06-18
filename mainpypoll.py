import csv

total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

with open('./election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        candidate = row[2]

        total_votes += 1

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1


print("----------------------------------------")
print("Election Results")
print("")
print(f"Total Votes: {total_votes}")
print("")

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")
