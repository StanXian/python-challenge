# Import os module and CSV files module
import os
import csv
csvpath = os.path.join("pyroll.csv")

#Creat list
vid = []
county = []
candidate = []

#creat variables
khan = 0
correy = 0
li = 0
otooley = 0

# Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #Loop
    for row in csvreader:
        vid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        #Count vote for each candidate
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

#Calculate winner
#creat two list of cndidates and thier votes
candidates = ["Khan", "Correy", "Li","O'Tooley"]
candidates_votes = [khan, correy, li, otooley]

#creat a dictionary that contain these two list
dict_c = dict(zip(candidates, candidates_votes))
winner = max(dict_c, key=dict_c.get)



#calculate and print
totalvoter = len(vid)

print("Election Results")
print("-----------------------")
print("Total Votes:" + str(totalvoter))
print("-----------------------") 
print("Khan: " + str(khan/totalvoter*100) + "%" + " (" + str(khan) + ")")
print("Correy: "  + str(correy/totalvoter*100) + "%" + " (" + str(correy) + ")")
print("Li: " + str(li/totalvoter*100) + "%" + " (" + str(li) + ")")
print("O'Tooley: " + str(otooley/totalvoter*100) + "%" + " (" + str(otooley) + ")")
print("-----------------------") 
print(f"Winner: {winner}")

#output text
output_file = ("Pypoll_Summary.txt")

with open(output_file,"w") as file:

 
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Votes:" + str(totalvoter))
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Khan: " + str(khan/totalvoter*100) + "%" + " (" + str(khan) + ")")
    file.write("\n")
    file.write("Correy: "  + str(correy/totalvoter*100) + "%" + " (" + str(correy) + ")")
    file.write("\n")
    file.write("Li: " + str(li/totalvoter*100) + "%" + " (" + str(li) + ")")
    file.write("\n")
    file.write("O'Tooley: " + str(otooley/totalvoter*100) + "%" + " (" + str(otooley) + ")")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("----------------------------")