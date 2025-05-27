# Assignment 3 - Using Decision Structures- Stockdale.

print("Welcome to the Travel Visa Eligibility Checker.")

# Get user input.
bank_balance = float(input("What is your bank balance in 3000USD)? "))
violent_felonies = int(input("How many violent felonies have you been "
                             "convicted of? "))
non_violent_felonies = int(input("How many non-violent felonies have you "
                                 "been convicted of? "))
visa_denials = int(input("How many times have you been denied a visa "
                         "before? "))
employed = input("Are you currently employed? (Yes/No): ").strip().capitalize()

# Decision structure.
if bank_balance < 3000:
    print("❌ You are not eligible: Your bank balance is too low.")
elif violent_felonies > 0:
    print("❌ You are not eligible: Too many violent felonies.")
elif non_violent_felonies > 2:
    print("❌ You are not eligible: Too many non-violent felonies.")
elif visa_denials > 2:
    print("❌ You are not eligible: Too many previous visa denials.")
elif employed != "Yes":
    print("❌ You are not eligible: You must be currently employed.")
else:
    print("✅ Congratulations! You are eligible for a tourist visa.")


# Second Practice Program Using Peru's real visa requirements.
''' The requirements to get into Peru are that: your 
passport is valid for at least 6 months; there is proof of round trip tickets
within 186 days; you have proof of accomodations for the trip; you have 
bank statements from your country of origin or a non-Peruvian bank; and that
you do not have a criminal record (although this is not super clear)'''

print("Welcome to the Peru Tourist Visa Eligibility Checker.")

# Get user input.
passport_validity = int(input("How many months until your passport expires? "))
round_trip_ticket = input("Do you have a round-trip ticket? (Yes/No): ") \
    .strip().capitalize()
accommodation = input("Do you have a hotel booking, tour package, or an "
                      "invitation letter? (Yes/No): ").strip().capitalize()
bank_statements = input("Can you provide recent bank statements? (Yes/No): ") \
    .strip().capitalize()
criminal_record = input("Do you have a criminal record? (Yes/No): ") \
    .strip().capitalize()

# Decision structure.
if passport_validity < 6:
    print("❌ You are NOT eligible: Your passport must be valid for at least "
          "6 months.")
elif round_trip_ticket != "Yes":
    print("❌ You are NOT eligible: A round-trip ticket is required.")
elif accommodation != "Yes":
    print("❌ You are NOT eligible: You must provide proof of accommodation "
          "or an invitation letter.")
elif bank_statements != "Yes":
    print("❌ You are NOT eligible: Recent bank statements are required to "
          "show financial solvency.")
elif criminal_record == "Yes":
    print("❌ You are NOT eligible: A clean criminal record is required.")
else:
    print("✅ Congratulations! You are eligible to apply for a tourist visa "
          "to Peru.")


# Third practice using a list to validate one of the criteria.

# List of visa-exempt countries (not complete - strictly for class).
visa_exempt_countries = [
    "United States", "Canada", "United Kingdom", "Germany",
    "France", "Japan", "Australia", "Brazil", "Argentina", "Mexico"
]

print("Welcome to the Peru Tourist Visa Eligibility Checker.")

# Get user input.
citizenship = input("What is your country of citizenship? ").strip().title()

if citizenship in visa_exempt_countries:
    print(f"300As a citizen of {citizenship}, you do not need a tourist visa "
          "for stays up to 90 days.")
else:
    print(f"Citizens of {citizenship} require a visa. Let's check your "
          "eligibility.")

    passport_validity = int(input("How many months until your passport "
                                  "expires? "))
    round_trip_ticket = input("Do you have a round-trip ticket? (Yes/No): ") \
        .strip().capitalize()
    accommodation = input("Do you have a hotel booking or invitation letter? "
                          "(Yes/No): ").strip().capitalize()
    bank_statements = input("Can you provide recent bank statements? "
                            "(Yes/No): ").strip().capitalize()
    criminal_record = input("Do you have a criminal record? (Yes/No): ") \
        .strip().capitalize()

    # Decision structure.
    if passport_validity < 6:
        print("❌ Not eligible: Passport must be valid for at least 6 months.")
    elif round_trip_ticket != "Yes":
        print("❌ Not eligible: You must have a round-trip ticket.")
    elif accommodation != "Yes":
        print("❌ Not eligible: You must have a hotel booking or invitation.")
    elif bank_statements != "Yes":
        print("❌ Not eligible: You must provide bank statements.")
    elif criminal_record == "Yes":
        print("❌ Not eligible: A clean criminal record is required.")
    else:
        print("✅ You are eligible to apply for a tourist visa to Peru.")
