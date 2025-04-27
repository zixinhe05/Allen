def music(size,*toppings):
    print(f"I can play {size} music like:")
    for topping in toppings:
        print("\n-{topping}")
def city(place,food,**information):
    information['where'] = place
    information['traditional_food'] = food
    return information
city('chengdu', "hot pot", location="at the southwest of China", relationship = "my hometown")
music(12,"piano","piano2")
