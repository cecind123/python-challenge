#import dependencies
import os
import csv

#Specify csv file
csvpath = os.path.join("employee_data.csv")

#create lists
emp_id = []
first_name = []
last_name = []
dob =[]
ssn = []
state = []

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
        emp_id.append(row["Emp ID"])
        first_name.append(row["Name"].split(" ")[0])
        last_name.append(row["Name"].split(" ")[1])
        dob.append(row["DOB"].split("-")[1] + "/" + row["DOB"].split("-")[2] + "/" + row["DOB"].split("-")[0])
        ssn.append("***-**-" + row["SSN"].split("-")[2])
        state.append(us_state_abbrev[row["State"]])
        
#Zip the info from lists
new_employee_data = zip(emp_id, first_name, last_name, dob, ssn, state)   

#Create new output csv file
output_path = os.path.join("new_employee_data.csv")

#Write new info into the new csv
with open(output_path, 'w', newline='') as new_csvfile:
    writer = csv.writer(new_csvfile, delimiter=",")
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(new_employee_data)
