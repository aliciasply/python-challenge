# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

voter_list = []
voter_count = 0

#create a dictionary to hold the candidate's names
candidate_list = {}


# Open the CSV 
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
      
    #this code is to get the value from the key candidate_list[candidate] 
    # Read each row of data after the header
    for row in csvreader:
       #voter_id = str(row[0])
        voter_count += 1
        candidate = row[2]
        if candidate in candidate_list:
            candidate_list[candidate] += 1
        else:
            candidate_list[candidate] = 1

print("Election Results")
print("--------------------------")
# The total number of votes cast
print(f'Total Votes: {voter_count}')  
print("--------------------------")

for candidate in candidate_list:

#set value as vote_number and put it back in the print statement after
    vote_number = candidate_list[candidate] 
    vote_percentage = "{:.3f}".format(vote_number/voter_count*100) 
    #print("{:.3f}".format(vote_percentage))

    print(f'{candidate}: {vote_percentage}% ({vote_number})')

# A complete list of candidates who received votes
# print(candidate_list)    
print(f'{candidate}: {vote_percentage}% ({vote_number})')  

# The winner of the election based on popular vote.
#example from stackoverflow - max(stats, key=stats.get) the stats in here is the dictionary
print("--------------------------")
#print(max(candidate_list, key=candidate_list.get))
print(f'Winner: {max(candidate_list, key=candidate_list.get)}')
print("--------------------------")

# output = ("Election Results\n"
# "--------------------------\n"
# f'Total Votes: {voter_count}\n'
# "--------------------------\n"

# f'{candidate}: {vote_percentage}% ({vote_number}\n'
# "--------------------------\n"
# f'Winner: {max(candidate_list, key=candidate_list.get)}\n'
# "--------------------------")

# print(output)
# with open ("analysis/output.txt", "w") as txt: 
#     txt.write(output)
