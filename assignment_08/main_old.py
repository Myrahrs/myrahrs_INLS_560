import sys  # For clean program exit
import os  # For platform-independent file path handling
import csv


def find(file_variable, search_variable):
    """
    Search for a term in the specified CSV file and optionally display matching entries.
    """
    search_variable = search_variable.lower()  # Normalize search term to lowercase
    matched_rows = []

    # Open file with utf-8 encoding and use csv.DictReader to handle CSV properly
    with open(file_variable, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames  # Get headers for printing later

        for row in reader:
            # Check if any field in the row contains the search term (case insensitive)
            if any(search_variable in (str(value).lower()) for value in row.values()):
                matched_rows.append(row)

    if matched_rows:
        print(f'Your search term "{search_variable}" exists in the {file_variable} file!')

        see_entries = input('Would you like to see the entries? (y or n)? ').lower()

        if see_entries == 'y':
            print(f'Here are all of the entries with the term "{search_variable}":')
            # Print headers as CSV line
            print(','.join(headers))

            for row in matched_rows:
                # Print row values joined by commas, properly handling commas inside fields by quoting them
                # Using csv module to write to string for correct quoting:
                from io import StringIO
                output = StringIO()
                writer = csv.DictWriter(output, fieldnames=headers)
                writer.writerow(row)
                print(output.getvalue().strip())  # Print CSV formatted row

        elif see_entries == 'n':
            print('Goodbye')
            sys.exit()

        else:
            print("Invalid option. Please enter 'y' or 'n'.")
    else:
        print(f'The term "{search_variable}" was NOT found in the file.')

def main():
    base_path = os.path.join('assignment_08')

    while True:
        file_choice = input(
            'What file would you like to search?:\n'
            'a) Animals\n'
            'b) 2000-2009 Top Music Charts\n'
            'x) to Exit\n'
        ).lower()

        if file_choice == 'x':
            print("Exiting program.")
            sys.exit()
        elif file_choice == 'a':
            file_variable = os.path.join(base_path, 'animals.csv')
        elif file_choice == 'b':
            file_variable = os.path.join(base_path, 'music.csv')
        else:
            print('Invalid option. Please select a, b, or x.')
            continue

        search_variable = input(f'Enter the search term for {file_variable} file: ').strip()

        find(file_variable, search_variable)

if __name__ == "__main__":
    main()