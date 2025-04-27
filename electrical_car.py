from car import Car
class Battery:
 """A simple attempt to model a battery for an electric car."""
 def __init__(self, battery_size=40):
   self.battery_size = battery_size
   def describe_battery(self):
    print(f"This car has a {self.battery_size}-kWh battery.")
def get_range(self):
 """Print a statement about the range this battery provides."""
 if self.battery_size == 40:
   range = 150
 elif self.battery_size == 65:
   range = 225
 print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
 """Models aspects of a car, specific to electric vehicles."""
 def __init__(self, make, model, year):
   super().__init__(make, model, year)
   self.battery = Battery()