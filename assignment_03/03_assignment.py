# Assignment 3 - Stockdale.
# Constants.
MIN_BANK_BALANCE = 3000
MAX_VIOLENT_FELONIES = 0
MAX_NON_VIOLENT_FELONIES = 2
MAX_VISA_DENIALS = 2
EMPLOYMENT_REQUIRED = "Yes"

# Introduction.
print("Welcome to the Enhanced Travel Visa Eligibility Checker.")
print("With just 5 pieces of information, you'll know your tourist visa "
      "eligibility")

# User input variables.
try:
    bank_balance = float(input("Enter your current bank balance (USD): "))
    violent_felonies = int(input("How many violent felonies have you been "
                                 "convicted of? "))
    non_violent_felonies = int(input("How many non-violent felonies have you "
                                     "been convicted of? "))
    visa_denials = int(input("How many times have you been denied a visa "
                             "before? "))
    employed = input("Are you currently employed? (Yes/No): ").strip().capitalize()

    # Check each condition.
    eligible = True
    if bank_balance < MIN_BANK_BALANCE:
        eligible = False
    if violent_felonies > MAX_VIOLENT_FELONIES:
        eligible = False
    if non_violent_felonies > MAX_NON_VIOLENT_FELONIES:
        eligible = False
    if visa_denials > MAX_VISA_DENIALS:
        eligible = False
    if employed != EMPLOYMENT_REQUIRED:
        eligible = False

    # Output results.
    if eligible:
        print("\nCongratulations! You meet all the requirements for a "
              "tourist visa.")
    else:
        print("\nUnfortunately, you do NOT meet the requirements for a "
              "tourist visa.")
        print("\nHere are the visa eligibility requirements:")
        print(f"- Minimum Bank Balance: ${MIN_BANK_BALANCE}")
        print(f"- Maximum Violent Felonies: {MAX_VIOLENT_FELONIES}")
        print(f"- Maximum Non-Violent Felonies: {MAX_NON_VIOLENT_FELONIES}")
        print(f"- Maximum Visa Denials: {MAX_VISA_DENIALS}")
        print(f"- Employment Status Required: {EMPLOYMENT_REQUIRED}")

        # Explain why they didn't qualify
        print("\nBased on your inputs:")
        if bank_balance < MIN_BANK_BALANCE:
            print(f"  - Your bank balance of ${bank_balance} is below the "
                  f"required ${MIN_BANK_BALANCE}.")
        if violent_felonies > MAX_VIOLENT_FELONIES:
            print(f"  - You have {violent_felonies} violent felony(ies), which "
                  f"exceeds the limit of {MAX_VIOLENT_FELONIES}.")
        if non_violent_felonies > MAX_NON_VIOLENT_FELONIES:
            print(f"  - You have {non_violent_felonies} non-violent felony(ies), "
                  f"which exceeds the limit of {MAX_NON_VIOLENT_FELONIES}.")
        if visa_denials > MAX_VISA_DENIALS:
            print(f"  - You have been denied a visa {visa_denials} time(s), "
                  f"which exceeds the limit of {MAX_VISA_DENIALS}.")
        if employed != EMPLOYMENT_REQUIRED:
            print(f"  - Employment required: {EMPLOYMENT_REQUIRED}, but your "
                  f"status is '{employed}'.")

except ValueError:
    print("Invalid input detected. Please enter valid numbers where requested.")
