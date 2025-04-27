my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("good")
for food in friend_foods:
    print(f"friend's favorite are {food}\n")
print(my_foods)