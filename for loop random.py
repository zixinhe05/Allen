import random

class Die:
    def __init__(self, sides=6):
        """Initialize the Die with a default of 6 sides."""
        self.sides = sides

    def roll_die(self):
        """Roll the die and return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

# Create a 6-sided die
six_sided_die = Die()

# Roll the 6-sided die 10 times
print("Rolling the 6-sided die 10 times:")
for _ in range(10):
    print(six_sided_die.roll_die())

# Create a 10-sided die
ten_sided_die = Die(sides=10)

# Roll the 10-sided die 10 times
print("\nRolling the 10-sided die 10 times:")
for _ in range(10):
    print(ten_sided_die.roll_die())

# Create a 20-sided die
twenty_sided_die = Die(sides=20)

# Roll the 20-sided die 10 times
print("\nRolling the 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided_die.roll_die())
