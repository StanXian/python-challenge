# Import os module and CSV files module
import os
import csv
csvpath = os.path.join("pybank.csv")

# Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #count total Months
    totalMonths = sum(1 for row in csvreader) -1   
    #print(totalMonths)

    #count net total amount of "Profit/Losses" 
    totalamount = 
    #count average of the changes 
    #count greatest increase
    #count greatest decrease
