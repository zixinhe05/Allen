from restaurant import Restaurant
class Staff:
    def __init__(self, staff=50):
        self.staff = staff
    def describe_staff(self):
        print(f'the number of staff in this restaurant is {self.staff}')
class good_restaurant(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.staff = Staff()