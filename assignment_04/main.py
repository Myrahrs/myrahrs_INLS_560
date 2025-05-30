# Homework 4 - Stockdale.

# Pet Store Item List
items = ['collar', 'leash', 'treats', 'bowl', 'bed',
         'toys', 'shampoo', 'litter', 'crate', 'food']

#For loop related to the items.
for item in items:
    if item == "treats":
        print(f"{item.upper()} - {len(item)} letters (a favorite!)")
        # Makes treats upper case, notates the length of the word (len)
        # and that it is a favorite.
    else:
        print(f"{item} - {len(item)} letters")
        # All other items in the list are regular case and tell the length of
        # the words using len.

