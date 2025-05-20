#May 19 Practice
# Get the Desired future value (FV).
future_value = float(input('Enter the desired future value: '))

# Get the Annual interest rate.
rate = float(input('Enter the annual interest rate: '))

# Get the Number of Years that the Money will Appreciate.
years = int(input('Enter the number of years the money will grow: '))

# Calculate the Amount Needed to Deposit.
present_value = future_value / (1.0 + rate)**years

# Display the Amount Needed to Deposit.
print('You will need to deposit this amount:', present_value)