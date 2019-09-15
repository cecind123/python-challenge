import os
import csv

csvpath = os.path.join("budget_data.csv")

total_months = []
total_profit = []
date = []
monthly_profit_change = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header= next(csvfile)

    for row in csvreader:
            total_months.append(row[0])
            total_profit.append(int(row[1]))
            
            #Find Net Profit
            net_profit = sum(total_profit)
            date.append(row[0])
            
            #Find Date of Greatest Increase & Decrease
            increase_date = total_profit.index(max(total_profit))
            decrease_date = total_profit.index(min(total_profit))

    for i in range(len(total_profit)-1):

    #Find difference between two months
            monthly_profit_change.append(total_profit[i+1]-total_profit[i])

    #Print analysis
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: {}".format(len(total_months)))
    print("Net Profit: ${}".format(net_profit))
    print("Average Change: {}".format(round(sum(monthly_profit_change)/len(monthly_profit_change),2)))
    print("Greatest Increase in Profits: {} (${})".format((date[increase_date]),max(monthly_profit_change)))
    print("Greatest Decrease in Profits: {} (${})".format((date[decrease_date]),min(monthly_profit_change)))

    
#Create txt file    
outpath = os.path.join("budget_analysis.txt")

#Write analysis into txt file
with open(outpath, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("-----------------------------------")
    datafile.write("\n")
    datafile.write("Total Months: {}".format(len(total_months)))
    datafile.write("\n")
    datafile.write("Net Profit: ${}".format(net_profit))
    datafile.write("\n")
    datafile.write("Average Change: {}".format(round(sum(monthly_profit_change)/len(monthly_profit_change),2)))
    datafile.write("\n")
    datafile.write("Greatest Increase in Profits: {} (${})".format((date[increase_date]),max(monthly_profit_change)))
    datafile.write("\n")
    datafile.write("Greatest Decrease in Profits: {} (${})".format((date[decrease_date]),min(monthly_profit_change)))
    