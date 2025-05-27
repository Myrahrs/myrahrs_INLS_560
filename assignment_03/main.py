# This program determines whether someone can adopt a cat.

# Constants.
MIN_SALARY = 55000.0    # Minimum annual salary
MIN_YEARS = 2           # Minimum years of continuous employment
MAX_PETS = 7            # Maximum number of other pets allowed
ALLERGIES = "No"        # Expected answer for allergies
OWN_RENT = "Own"        # Expected home ownership status

# User inputs.
salary = float(input("Enter your annual salary: "))

years_on_job = int(input(f"Enter the number of years you have been"
                         f"continuously employed"))

num_other_pets = int(input("How many other pets do you have? "))

allergy = input("Are you allergic to cats? (Yes/No): ").strip().capitalize()

house_ownership = input("Do you rent or own your home? ").strip().capitalize()

# Determine whether the person qualifies.
if salary < MIN_SALARY:
    print(f"You must earn at least ${MIN_SALARY:.2f} annually to"
          f"adopt a cat.")
elif years_on_job < MIN_YEARS:
    print(f"You must have at least {MIN_YEARS} years of employment.")
elif num_other_pets > MAX_PETS:
    print(f"You cannot have more than {MAX_PETS} other pets.")
elif allergy != ALLERGIES:
    print("Unfortunately, cat allergies prevent adoption eligibility.")
elif house_ownership != OWN_RENT:
    print("You must own your home to adopt a cat.")
else:
    print("Congratulations! You are eligible to adopt a cat.")

# Assignment using AND, not ELIF (it is commented out)
'''# This program determines whether someone can adopt a cat

# Constants.
MIN_SALARY = 45000.0
MIN_YEARS = 2
MAX_PETS = 7
ALLERGIES = "No"
OWN_RENT = "Own"

# User inputs.
salary = float(input("Enter your annual salary: "))
years_on_job = int(input("Enter the number of years employed: "))
num_other_pets = int(input("How many other pets do you have? "))
allergy = input("Are you allergic to cats? (Yes/No): ").strip().capitalize()
house_ownership = input("Do you rent or own your home? ").strip().capitalize()

# Decision using `and`.
if (salary >= MIN_SALARY and
        years_on_job >= MIN_YEARS and
        num_other_pets <= MAX_PETS and
        allergy == ALLERGIES and
        house_ownership == OWN_RENT):
    print("Congratulations! You are eligible to adopt a cat.")
else:
    print("You are not eligible to adopt a cat. See below:")

    if salary < MIN_SALARY:
        print(f"- Your salary of ${salary:.2f} is below the required ${MIN_SALARY}.")
    if years_on_job < MIN_YEARS:
        print(f"- You must have at least {MIN_YEARS} years of employment.")
    if num_other_pets > MAX_PETS:
        print(f"- You have too many pets. The limit is {MAX_PETS}.")
    if allergy != ALLERGIES:
        print("- Cat allergies disqualify you from adoption.")
    if house_ownership != OWN_RENT:
        print("- You must own your home to adopt a cat.")
'''
