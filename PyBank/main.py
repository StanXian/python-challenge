# Import os module and CSV files module
import os
import csv
csvpath = os.path.join("pybank.csv")

#Creat two list to collect amount and change
month = []
amount = []
change = []

# Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    totalMonth = 0
    totalAmount = 0
    

    #loop
    for row in csvreader:

        #count for each variables
        totalAmount = totalAmount + float(row[1])
        totalMonth += 1
        amount.append(float(row[1]))
        month.append(row[0])
       
        
    #calculate change
    #loop through list amount
    for i in range(totalMonth - 1):    

        change.append(amount[i+1]-amount[i])

    #calculate the ave in change 
    ave = sum(change)/len(change)

    #find extreme value in change
    inc = max(change)  
    dec = min(change)

    #find the month when extreme value exist
    incmonth = change.index(inc) + 1
    decmonth = change.index(dec) + 1

    #print
    print("Finanxial Analysis")
    print("-------------------------")
    print("Total Months:" + str(totalMonth))
    print("Total: $" + str(totalAmount))
    print("Average Change: $" + str(ave))
    print("Greatest Increase in Profit:" + str(month[incmonth]) + " " + "($" + str(inc) + ")")
    print("Greatest Decrease in Profit:" + str(month[decmonth]) + " " + "($" + str(dec) + ")")
    
#output file
output_file = ("Pybank_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Months:" + str(totalMonth))
    file.write("\n")
    file.write("Total: $" + str(totalAmount))
    file.write("\n")
    file.write("Average Change: $" + str(ave))
    file.write("\n")
    file.write("Greatest Increase in Profit:" + str(month[incmonth]) + " " + "($" + str(inc) + ")")
    file.write("\n")
    file.write("Greatest Decrease in Profit:" + str(month[decmonth]) + " " + "($" + str(dec) + ")")
    
