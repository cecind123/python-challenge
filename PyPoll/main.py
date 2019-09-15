import os
import csv

csvpath = os.path.join("election_data.csv")

total_votes = []
candidates = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header= next(csvfile)
    
    for row in csvreader:
            total_votes.append(row[0])
            candidates.append(row[2])

    def winner(candidates):
        return max(set(candidates), key = candidates.count)
    
    print("Election Results")
    print("---------------------------")
    print("Total # of Votes: {}".format(len(total_votes)))
    print("---------------------------")
    print("Khan: {:.3f}% ({})".format((candidates.count("Khan")/len(total_votes))*100,candidates.count("Khan")))    
    print("Correy: {:.3f}% ({})".format((candidates.count("Correy")/len(total_votes))*100,candidates.count("Correy")))
    print("Li: {:.3f}% ({})".format((candidates.count("Li")/len(total_votes))*100,candidates.count("Li")))
    print("O'Tooley: {:.3f}% ({})".format((candidates.count("O'Tooley")/len(total_votes))*100,candidates.count("O'Tooley")))
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
    datafile.write("Khan: {:.3f}% ({})".format((candidates.count("Khan")/len(total_votes))*100,candidates.count("Khan")))    
    datafile.write("\n")
    datafile.write("Correy: {:.3f}% ({})".format((candidates.count("Correy")/len(total_votes))*100,candidates.count("Correy")))
    datafile.write("\n")
    datafile.write("Li: {:.3f}% ({})".format((candidates.count("Li")/len(total_votes))*100,candidates.count("Li")))
    datafile.write("\n")
    datafile.write("O'Tooley: {:.3f}% ({})".format((candidates.count("O'Tooley")/len(total_votes))*100,candidates.count("O'Tooley")))
    datafile.write("\n")
    datafile.write("---------------------------")
    datafile.write("\n")
    datafile.write("Winner: {}".format(winner(candidates)))
    datafile.write("\n")
    datafile.write("---------------------------")