# June 2, 2025 Functions 2
def make_pizza(*toppings):  #arbitrary arguments have one *.
    print("<ol>")
    for topping in toppings:
        print(f" <li> {topping} </li>")
    print("</ol>")

make_pizza('mushroom', 'mushroom', 'pineapple', 'pepperoni')

# Kwargs.
def pup_details(name, **details):   #kwarg is a keyword arbitrary arguments
    "Captures  arbitrary doggy details in a dictionary format"
    print(f"Pup Details for {name}:")
    for key, value in details.items():
        print(f" {key}: {value}")
    print('\n')
    
pup_details('Rosie', weight=60, color='brown', YOB='2020', owner='Annie')
pup_details('Luna', color='black', lbs=25, year_born=2023)

