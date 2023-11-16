# Path to csv.
import csv
csv_path = "Resources/budget_data.csv"

# Create your lists to store dates and profits/losses.
dates = []
profits_losses = []

# Reading the csv file using a with statement to 
# make sure it closes after its been read each time.
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# calculate total number of months included in the dataset. 
# Printed at bottom
total_months = len(dates)

# calculate the net total amount of "Profit/Losses" over the entire period.
# Printed at bottom
net_total = sum(profits_losses)

# calculate the changes of "Profit/Losses" over the whole period, and then the average
# of those changes.

changes = []
for i in range(len(profits_losses) - 1):
    change = profits_losses[i + 1] - profits_losses[i]
    changes.append(change)

# Calculate the average change
total_changes = sum(changes)
average_change = total_changes / len(changes)

# Find the greatest increase in profits, add 1 at the end to get the next month.
max_increase = max(changes)
index_of_max_increase = changes.index(max_increase)
date_of_max_increase = dates[index_of_max_increase + 1]

# Do the same for greatest decrease.
min_decrease = min(changes)
index_of_min_decrease = changes.index(min_decrease)
date_of_min_decrease = dates[index_of_min_decrease + 1]

# printing the code! I found out that using \n is a neat way to make the data more presentable.
# creating an output 'summary' so that I can export all of it to a text file.

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    "\nGreatest Increase in Profits: "
    f"Date: {date_of_max_increase} "
    f"Amount: {max_increase}"
    "\nGreatest Decrease in Profits: "
    f"Date: {date_of_min_decrease} "
    f"Amount: {min_decrease}")

print(output)

# Export the results to text file.
file_to_output = "output.txt"
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)