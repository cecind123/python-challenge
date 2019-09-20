#import dependencies
import os
import csv

#Specify csv file
csvpath = os.path.join("employee_data.csv")

#create lists
EmpId = []
FirstName = []
LastName = []
DOB =[]
SSN = []
State = []

#Establish state abbreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#open csv file 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    #append the re-written info into the lists created
    for row in csvreader:
        EmpId.append(row["Emp ID"])
        FirstName.append(row["Name"].split(" ")[0])
        LastName.append(row["Name"].split(" ")[1])
        DOB.append(row["DOB"].split("-")[1] + "/" + row["DOB"].split("-")[2] + "/" + row["DOB"].split("-")[0])
        SSN.append("***-**-" + row["SSN"].split("-")[2])
        State.append(us_state_abbrev[row["State"]])
        
#Zip the info from lists
new_employee_data = zip(EmpId, FirstName, LastName, DOB, SSN, State)   

#Create new output csv file
output_path = os.path.join("new_employee_data.csv")

#Write new info into the new csv
with open(output_path, 'w', newline='') as new_csvfile:
    writer = csv.writer(new_csvfile, delimiter=",")
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(new_employee_data)
