import os
import csv

# Specify the file to write to
pypoll_path = os.path.join("pypoll" , "analysis")

# Open the file using "write" mode. Specify the variable to hold the contents
poll1 = open ("output.txt", "w") 
L = ["Election Results \n",
    "-------------------------- \n", 
    "Total Votes: 3521001 \n",
    "-------------------------- \n",
    "Khan: 63.000% (2218231) \n",
    "Correy: 20.000% (704200) \n",
    "Li: 14.000% (492940) \n",
    "Khan: 63.000% (2218231) \n",
    "O'Tooley: 3.000% (105630) \n",
    "-------------------------- \n",
    "Winner: Khan \n",
    "--------------------------"]

poll1.writelines(L)






