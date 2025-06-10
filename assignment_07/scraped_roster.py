# Stockdale Assignment 7.

# PRE_ASSIGNMENT
# Scrape entire men's basketball roster from Campbell University
# (UNC's page is dynamic and cannot use BeautifulSoup)
# Extract player data: jersey number, class year, position, height,
# weight, hometown, high school
# Unfortunately, name cannot be pulled
# Calculate BMI from height and weight

# Campbell Fighting Camels 2024 Roster Scraper from Sports Reference
# This script scrapes the roster table from Sports Reference college
# basketball site and saves the data into a CSV file.
# It uses requests and BeautifulSoup.

import requests  # For sending HTTP requests to fetch webpage content
from bs4 import BeautifulSoup  # For parsing HTML and extracting elements
import pandas as pd  # For handling tabular data and exporting CSV files


# Step 1: Define the URL of Campbell Fighting Camels 2024 roster page
url = "https://www.sports-reference.com/cbb/schools/campbell/2024.html"

# Step 2: Make an HTTP GET request to fetch the webpage HTML content
response = requests.get(url)

# Step 3: Check if the GET request was successful (status code 200 = OK)
if response.status_code != 200:
    print(f"Failed to retrieve page, status code: {response.status_code}")
    exit(1)  # Exit if the page cannot be loaded

# Step 4: Parse the retrieved HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Locate the roster table by looking for the <table> element with id="roster"
table = soup.find("table", id="roster")

# Step 6: Defensive check - if table is not found, inform and exit
if not table:
    print("Roster table not found on the page.")
    exit(1)

# Step 7: Extract the header names from the table's <thead> section (optional)
headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

# Step 8: Extract all player rows from the table's <tbody> section
rows = table.find("tbody").find_all("tr")

# Step 9: Initialize an empty list to store player data dictionaries
roster_list = []

# Step 10: Loop through each row to extract player details
for row in rows:
    # Extract all <td> elements (table cells) in the current row
    cols = row.find_all("td")

    # Skip rows without any <td> cells (could be header or empty rows)
    if not cols:
        continue

    # Step 11: Create a dictionary mapping the relevant data fields
    player_dict = {
        "jersey_number": cols[0].get_text(strip=True),
        "class_year": cols[1].get_text(strip=True),
        "position": cols[2].get_text(strip=True),
        "height": cols[3].get_text(strip=True),  # e.g., '6-4'
        "weight_lbs": cols[4].get_text(strip=True),
        "hometown": cols[5].get_text(strip=True),
        "high_school": cols[6].get_text(strip=True),
        # height_in will be computed later
    }

    # Step 12: Add this player's dictionary to the list
    roster_list.append(player_dict)

# Step 13: Convert the list of player dictionaries into a pandas DataFrame
df = pd.DataFrame(roster_list)


def height_to_inches(height_str):
    """Convert height string like '6-4' to inches (e.g., 76)."""
    try:
        feet, inches = height_str.split('-')
        return int(feet) * 12 + int(inches)
    except Exception:
        return None


# Step 14: Apply the height conversion function to create a 'height_in' column
df["height_in"] = df["height"].apply(height_to_inches)

# Step 15: Convert weight column from strings to numeric, coercing errors to NaN
df["weight_lbs"] = pd.to_numeric(df["weight_lbs"], errors="coerce")

# Step 16: Calculate Body Mass Index (BMI) using the formula:
# BMI = (weight in pounds * 703) / (height in inches)^2
df["BMI"] = df.apply(
    lambda row: (703 * row["weight_lbs"]) / (row["height_in"] ** 2)
    if pd.notnull(row["weight_lbs"]) and pd.notnull(row["height_in"])
    else None,
    axis=1,
)

# Step 17: Export the resulting DataFrame to a CSV file (no index)
df.to_csv("campbell_fighting_camels_2024_roster.csv", index=False)

# Step 18: Print confirmation and show the first few rows as a preview
print(
    "Roster data successfully scraped and saved to "
    "'campbell_fighting_camels_2024_roster.csv'."
)
print(df.head())