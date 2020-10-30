# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Pypoll", "Resources", "election_data.csv")

# Open the CSV 
with open(csvpath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
       print(row)

def count_votes(election_data):
    for 

