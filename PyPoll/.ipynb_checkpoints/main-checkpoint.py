#import dependencies
import os
import csv

#Specify csv file
csvpath = os.path.join("election_data.csv")

#create lists
total_votes = []
candidates = []
UniqueNames = []

#open csv file 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header= next(csvfile)
    
    #append the information into the lists created
    for row in csvreader:
            total_votes.append(row[0])
            candidates.append(row[2])
            
            #identify unique names in the candidate list
            if row[2] not in UniqueNames:
                UniqueNames.append(row[2])
            
    #create a function that finds the candidate with the most votes    
    def winner(candidates):
            return max(set(candidates), key = candidates.count)
    
   #Print Results
    print("Election Results")
    print("---------------------------")
    print("Total # of Votes: {}".format(len(total_votes)))
    print("---------------------------")
    for name in UniqueNames:
        print("{}: {:.3f}% ({})".format(name,(candidates.count(name)/len(total_votes))*100,candidates.count(name)))        
    print("---------------------------")
    print("Winner: {}".format(winner(candidates)))
    print("---------------------------")
    
    
#Create txt file
outpath = os.path.join("election_results.txt")

#Write analysis into txt file
with open(outpath, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    datafile.write("Election Results")
    datafile.write("\n")
    datafile.write("---------------------------")
    datafile.write("\n")
    datafile.write("Total # of Votes: {}".format(len(total_votes)))
    datafile.write("\n")
    datafile.write("---------------------------")
    datafile.write("\n")
    for name in UniqueNames:
        datafile.write("{}: {:.3f}% ({})\n".format(name,(candidates.count(name)/len(total_votes))*100,candidates.count(name)))
    datafile.write("---------------------------")
    datafile.write("\n")
    datafile.write("Winner: {}".format(winner(candidates)))
    datafile.write("\n")
    datafile.write("---------------------------")