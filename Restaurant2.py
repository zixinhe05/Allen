class Restaurant:
     def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 10
     def describe(self):
        print(f"{self.name} is famous for its hotpots.")
     def opens(self):
        print(f"{self.name} is open!")
     def read_served(self):
         print(f"The restaurant serves {self.number_served} customres")
     def updated_served(self, numbers):
         if numbers >= self.number_served:
             self.number_served = numbers
         else:
             print("you can't reduce the numbers of customres")
     def increment_served(self, numberss):
         self.number_served += numberss
my_restaurant = Restaurant('Chengdu', "buffet")

my_restaurant.updated_served(9)
my_restaurant.read_served()

my_restaurant.increment_served(100)
my_restaurant.read_served()

print(f"My restaurant's name is {my_restaurant.name}.")
print(f"My restaurant's type is {my_restaurant.type}.")