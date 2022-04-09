voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]



#run a for loop to get the keys and values of a dictionary
for county_dict in voting_data:
    print(county_dict)

#run a for loop to get the keys using range method
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# run a for loop over the list to get the values of the dictionary
for i in voting_data:
 for value in i.values():
     print(value)

# run a for loop to get the number of voters from each dictionary - this works but is not an option on quiz (I use i instead of county dict here)
for i in range(len(voting_data)):
    print(voting_data[i]['registered_voters'])


# run a for loop to get the number of voters from each dictionary - this works but is not an option on quiz

for county_dict in voting_data:

     print(county_dict['registered_voters'])



# print the county name 

for county_dict in voting_data:
    print(county_dict['county'])


