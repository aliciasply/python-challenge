# Modules
import os
import csv


# Set path for file
financial_csvpath = os.path.join("Resources", "budget_data.csv")

# set the value of month count to 1 as we just told the command to skip the month of Jan
month_count = 1
total = 0
month_increase = " "
month_decrease = " "
profit_increase = 0
losses_decrease = 0
change_list = []
change = 0
last_profit =0

# Open the CSV 
with open(financial_csvpath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
   #print(csvreader) if I want to show the file
    #skipping the first row 
    csv_header = next(csvreader)
    first_row = next(csvreader)
    # need to add the first row number because it wasnt counted
    total = total + int(first_row[1])
    last_profit = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
        month = str(row[0])  
        profit = int(row[1])
        month_count += 1
        total = total + profit
        change = profit - last_profit
        change_list.append(change)
        if change > profit_increase:
            profit_increase = change 
            month_increase = month
        elif change < losses_decrease:
            losses_decrease = change   
            month_decrease = month 
        # profit from feb for first interation    
        last_profit = profit     

# round up the number and with 2 decimal place
average = round(sum(change_list)/len(change_list), 2)
   
#print(len(change_list))
output = ("Financial Analysis\n"
"----------------------------------------------------\n"

# The total number of months included in the dataset
f'Total Months: {month_count}\n'

# The net total amount of "Profit/Losses" over the entire period
f'Total: ${total}\n'

# The average of the changes in "Profit/Losses" over the entire period
#round statement to round up and 2 is for 2 decimal
f'Average Changes: ${average}]\n'

# The greatest increase in profits (date and amount) over the entire period
f'Greatest Increase in Profits: {month_increase} (${profit_increase})\n'


# The greatest decrease in losses (date and amount) over the entire period
f'Greatest decrease in Profits: {month_decrease} (${losses_decrease})\n')

print(output)
with open ("analysis/output.txt", "w") as txt: 
    txt.write(output)

 

