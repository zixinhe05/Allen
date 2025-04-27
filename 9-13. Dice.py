import random

# Create a list with 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Randomly select 4 items from the list
selected_items = random.sample(items, 10)

# Print the selected items and the prize message
print(f"Selected items: {selected_items}")
print("Any ticket matching these 10 numbers or letters wins a prize!")
