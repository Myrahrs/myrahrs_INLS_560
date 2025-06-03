# ----------------------------------------------
# Custom Menu Program with a While Loop
# STOCKDALE
# PART A - Cat Supply Shop
# ----------------------------------------------

# Prime the loop with an empty variable
menu_option = ''

# Start the loop; keep running unless user types 'q'
while menu_option != 'q':
    # Display the menu options
    print(
        'MENU:',
        'a: check cat food inventory',
        'b: process litter box orders',
        'q: quit program',
        sep="\n"
    )

    # Prompt user input and assign to the variable
    menu_option = input("Enter a letter to choose an option: ")

    # Decision logic based on user input
    if menu_option == 'a':
        print("Fetching current inventory of kibble, cans, and treats...")
    elif menu_option == 'b':
        print("Shipping out the freshest litter boxes with paw-sitive care!")

# Exit message
print("Thanks for keeping our feline friends happy. Goodbye!")

# ----------------------------------------------
# Nested While Menu Example
# STOCKDALE
# PART B - Cat Supply Shop
# ----------------------------------------------

# Initialize the loop control variable
menu_option = ''

# Start the loop
while menu_option != 'q':
    # Multiline f-string menu
    print(f'''
Cat Shop FAQS:
a: check cat food inventory
b: process litter box orders
q: exit
''')

    # Get user input
    menu_option = input("Enter your choice (a, b, or q): ")

    # Logic for menu option 'a'
    if menu_option == 'a':
        print("Only certified cat-tenders can access the inventory database!")

    # Logic for menu option 'b' with nested input
    elif menu_option == 'b':
        has_gloves = input(
            "Do you have gloves for handling litter boxes? (y or n): "
        )
        if has_gloves == 'y':
            print("Purr-fect! You're all set to pack the cleanest boxes around.")
        else:
            print("No gloves? Better grab a pair before scooping!")

# Final message after quitting
print("Thanks for helping the Cat Shop! Meow for now.")