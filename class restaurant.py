class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        print(f"{self.name} is beautiful and famous for its hotpots")
    def open_restaurant(self):
        print(f'{self.name} is open right now')
my_restaurant = Restaurant("momingtang", "noodles")
print(f"my restaurant's name is {my_restaurant.name}")
my_restaurant.open_restaurant()
