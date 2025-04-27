def make_shirt(size, color):
    print(f'I need a {size} T-shirt')
    print(f'I like the {color} T-shirt')
make_shirt("medium","red")
def build_person(first_name, last_name, age=None):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 if age:
  person['age'] = age
 return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
