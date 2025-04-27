friend = {
    "first_name":"song",
    "last_name":"pei",
    "age":20,
    "city":"Chengdu"
    }
for it, iformation in friend.items():
    print(f'{it.title()} is {iformation}')
country_river ={
    "China":"yellow river",
    "America":"Pittsburgh's river",
    'nile': 'egypt'
    }
for country in country_river.keys():
    print(country)
for river in country_river.values():
    print(river)
Places = ['China','America']
for country in country_river.keys():
    print(f'I have visited {country}')
    if country in Places:
        river = country_river[country].title()
        print(f'\t{country} has beautiful {river}')