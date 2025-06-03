# June 2, 2025 Class - Pure String
"""taken procedural logic and 
refactoered it to work for any string"""
def count_user_chars(user_string, user_char):  
    count_chars = 0                                #start at 0.
    for char in user_string:
        if char.lower() == user_char.lower():
            count_chars = count_chars + 1
    return count_chars

print(count_user_chars('Bananas', 'e'))         #counting e's in the string.
