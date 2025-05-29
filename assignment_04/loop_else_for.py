numbers = [1, 2, 4, 5]

for num in numbers:
    if num == 3:
        print("Found number 3!")
        break
    print(f'Checked {num}')
else:
    print("The number 3 was not found.")
