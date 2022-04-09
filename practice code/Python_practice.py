# Practicing if statements - determine if the second county in the list is Denver

#declare the list of counties
counties = ["Arapahoe", "Denver", "Jefferson"]

# Check if Denver is the 2nd value in the list (this will return Denver)
if counties[1] == "Denver":
    print(counties[1])

# check if either "Arapahoe" or "El Paso" is in the counties list
if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else: 
    print("Arapahoe or El Paso is NOT in the list of counties")


# Decision statment using IN and AND/OR

# combine membership and logical operations to test certain conditions. determine if two counties, Arapahoe and El Paso, are in the list of counties.
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# check if either "Arapahoe" or "El Paso" is in the counties list.
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not in the list of counties.")


# 3.2.9 Quiz

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe in counties list")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# 3.2.10 - LOOPS

## Basic loop to print all counties in defined iterable of county
for county in counties:
    print(county)

## using ranges
for i in range(len(counties)):
    print(counties[i])









