# Path to csv.
import csv
csv_path = "Resources/election_data.csv"

# Store necessary variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the csv file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    # Loop through each row in the CSV file.
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]  

        # Count each candidate's votes.
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

# Determine the votes winner.
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Calculate each candidate's percentage of votes won. 
# Starting by defining a format and a results list.
percentage_format = "{:.3%}"
results = []

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    formatted_result = f"{candidate}: {percentage:.3f}% ({votes})"
    results.append(formatted_result)

# Print to terminal.
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file. 
# I found this alternate method using a with statement, and it makes more logical sense to me.
output_file_path = "output.txt"
with open(output_file_path, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------")
    for result in results:
        txt_file.write(result + "\n")
    txt_file.write("-------------------------")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------")
