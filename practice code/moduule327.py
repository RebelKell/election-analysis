

#  declare a list variable for counties
counties = ["Arapahoe","Denver","Jefferson"]

# Find the first and second items from the list (this will return a list containing a copy of the items in the list from the starting index value up to, but not including, the ending index value ) 
counties[0:2]

# Create/declare the dictionary
counties_dict = {}

# Add values to the keys 
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

# See how many counties are in the dictionary
len(counties_dict)

# See a list of the keys in the dictionary
counties_dict.keys()

# See a list of the values in the dictionary
counties_dict.values()

#prints (aka shows) what is in the dictionary - two methods
print(counties_dict)
counties_dict.items()

# Get a specific value from the list where the output will be the value of the key
counties_dict.get("Denver")

# CREATE A LIST OF DICTIONARIES


# Create an empty list
voting_data = []

#Then add, or append, each dictionary to the voting_data list with info from each county. FYI - .append takes only one argument. Is there a way to add multiple dictionaries to a list in one command?
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})


# See the output of the dictionary. This info will look like a csv with County and registered_voters being the headers and the name of the county and populations being the values in the rows
print(voting_data)


# get the length of the voting_data dictionaries
len(voting_data)

# Use indexing and slicing to get one or more dictionaries.
## this gets you Jefferson and their corresponding populations using indexing
voting_data[2]
## this gets you Arapahoe their corresponding populations using slicing
voting_data[0:1]
## this gets you Arapahoe and Denver and their corresponding populations using slicing     
voting_data[0:2]

# Use the append(), insert(), and remove() methods to add and remove one or more dictionaries.
## Append
voting_data.append({"county":"El Paso", "registered_voters": 495685})
## Insert
voting_data.insert(0,{"county":"Essex", "registered_voters": 345865})
## !! Remove (remove method) - FYI; you must add both the keys and values to remove entirely - THIS WILL NOT WORK: voting_data.remove("Essex")
voting_data.remove({"county":"Essex", "registered_voters": 345865})
voting_data.remove({'county': 'El Paso', 'registered_voters': 495685})

# Change a value for one of the keys in the list of dictionaries. Change Essex to Multnomah. Just changing the name will remove everything else, FYI
voting_data[0] = {"county":"Multnomah", "registered_voters": 345865}

# MODULE 3.2.7 QUIZ: 
## 1. Add the new county “El Paso” and its registered voters, 461149, to the second position in voting_data. 
voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
## 2. Remove “Arapahoe” and its registered voters from voting_data. 
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
## 3. Make “Denver” and its registered voters the third item in voting_data, but keep “Jefferson” and its registered voters as the second item. This takes multiple steps   
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Denver", "registered_voters": 463353})
## 4. Add “Arapahoe” and its registered voters to voting_data.
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

# 










    









