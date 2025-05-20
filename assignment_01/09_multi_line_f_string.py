'''
# In class quotation practice. 

     Sample Quote

        I once heard a wise man saying something that went like, "If at first you don't succeed, 
        reduce your expectations till your a success."

        —Shane Wighton
'''

# Create first name and a last name variable where the values are lowercase letters shane wighton.
# (When you print the quote you will use title case string method.)
first_name = 'Myrah'
last_name = 'Stockdale'

# Create a full name variable by concatenating the first name, a space, and the last name.
full_name = first_name + ' ' + last_name

# Create a varible that will hold the string literal that is not output in quotes. Leave out the comma. It will be in the f-string.
non_quote = 'I once heard a wise person saying something that went like this'

# Create a variable that will include the double quotes and contains a contraction. Escape the contraction.
quote = '"If at first you don\'t succeed, reduce your expectations until you are a success."'

# On one line, use the print function with an f-string by passing the non-quote variable, then the quote variable.
# Include two newline characters and an em-space Character (\u2014) then call the fullname variable and use the title method with dot notation.

print(f"{non_quote}: {quote}\n\n\u2015\u2015{full_name.title()}")

# print it again and this time using a multi-line f-string to avoid having to use the new line characters. 
# This makes it easier to code and read.

print('\n---------------------\n')

print(f'''{non_quote}: {quote}

――{full_name.title()}''')