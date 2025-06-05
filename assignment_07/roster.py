# Stockdale Assignment 7.
# PRE_ASSIGNMENT.
# Data from: https://goheels.com/sports/mens-basketball/roster.
# Code pandas install: pip install pandas -- in git bash.

# Step 1: Import pandas library for DataFrame operations.
import pandas as pd  

# Define player data as a list of dictionaries.
roster_data = [
    {
        "first_name": "Zyon",
        "last_name": "Pullin",
        "jersey_number": 1,
        "height": "6-4",
        "class_year": "Graduate"
    },
    {
        "first_name": "Seth",
        "last_name": "Trimble",
        "jersey_number": 0,
        "height": "6-3",
        "class_year": "Sophomore"
    },
    {
        "first_name": "Harrison",
        "last_name": "Ingram",
        "jersey_number": 55,
        "height": "6-7",
        "class_year": "Junior"
    },
    {
        "first_name": "RJ",
        "last_name": "Davis",
        "jersey_number": 4,
        "height": "6-0",
        "class_year": "Senior"
    },
    {
        "first_name": "Jae’Lyn",
        "last_name": "Withers",
        "jersey_number": 24,
        "height": "6-9",
        "class_year": "Graduate"
    },
    {
        "first_name": "Elliot",
        "last_name": "Cadeau",
        "jersey_number": 2,
        "height": "6-1",
        "class_year": "Freshman"
    },
    {
        "first_name": "Armando",
        "last_name": "Bacot",
        "jersey_number": 5,
        "height": "6-11",
        "class_year": "Graduate"
    },
    {
        "first_name": "Jalen",
        "last_name": "Washington",
        "jersey_number": 13,
        "height": "6-10",
        "class_year": "Sophomore"
    },
    {
        "first_name": "Creighton",
        "last_name": "Leblanc",
        "jersey_number": 11,
        "height": "6-5",
        "class_year": "Freshman"
    },
    {
        "first_name": "James",
        "last_name": "Okonkwo",
        "jersey_number": 32,
        "height": "6-8",
        "class_year": "Junior"
    }
]

# Step 3: Convert the list into a pandas DataFrame called df.
# This creates a structured table with specified column headers.
df = pd.DataFrame(roster_data)

# Step 4: Print the DataFrame.
print(df)


# EXTRA LEARNING.
# If you want the dataframe sorted by the last name key then you make a new. 
# variable and use sort values to define key/column to sort by.

# Sort by Last Name.
df_sorted_by_name = df.sort_values(by="last_name")
print("\nSorted by last name:")
print(df_sorted_by_name)

# Sort by jersey number (lowest to highest).
df_sorted_by_number = df.sort_values(by="jersey_number")
print("\nSorted by jersey number:")
print(df_sorted_by_number)