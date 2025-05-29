#  Nested Loop in Open Stax 
hour = 8
minute = 0

while hour <= 9:
    while minute < 60:
        print(f"{hour}:{minute:02d}") ## Correcting the single 0 to 00
        minute += 30
    hour += 1
    minute = 0