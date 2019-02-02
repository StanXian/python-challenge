# Import os module and CSV files module
import os
import csv
csvpath = os.path.join("pybank.csv")

# Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    totalMonth = 0
    x = 0

    #loop
    for row in csvreader:

        #count for each variables
        x = x + float(row[1])
        totalMonth += 1
        

    #print
    print(totalMonth)
    print(x)
    
        
    #count average of the changes 
    #count greatest increase
    #count greatest decrease
