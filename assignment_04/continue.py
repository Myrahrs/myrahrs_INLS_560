#Divisible by 9? Skip.
numbers=[24,81,200,1235,1500]

for num in numbers:
    if num % 9 ==0:
        print(f'Divisible by 9 Skipping:{num}')
        continue
    print(f"Processing {num}")