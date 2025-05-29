#Divisible by 9? Find First.
numbers=[24,81,200,1235,1500]

for num in numbers:
    if num % 9 ==0:
        print(f'Divisible by 9:{num}')
        break
    print(f"Processing {num}")