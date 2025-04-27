pizza = {
 'crust': ['thick',"circle"],
 'toppings': ['mushrooms', 'extra cheese'],
 }
for topping in pizza['toppings']:
    print(topping)
for n,L in pizza.items():
    print(f"{n}'s choices are")
    for l in L:
        print (f"\t{l.title()}")