# Assignment 3 - Using Decision Structures- Stockdale.

print("Welcome to the Travel Visa Eligibility Checker.")

# Get user input .
bank_balance = float(input("What is your bank balance in USD)? "))
violent_felonies = int(input("How many violent felonies have you been "
                             "convicted of? "))
non_violent_felonies = int(input("How many non-violent felonies have you "
                                 "been convicted of? "))
visa_denials = int(input("How many times have you been denied a visa "
                         "before? "))
employed = input("Are you currently employed? (Yes/No): ").strip().capitalize()

# Decision structure
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
