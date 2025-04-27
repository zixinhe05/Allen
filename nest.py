friends=[]
for friends_number in range(15):
    new_information={
    "first_name":"song",
    "last_name":"pei",
    "age":20,
    "city":"Chengdu"
    }
    friends.append(new_information)
for friend in friends[:6]:
    print(friend)
print(len(friends))
for friend in friends:
    if friend['first_name']=="song":
        friend['first_name']="pei"
        friend["last_name"]="gong"
for friend in friends[:5]:
    print(friend)


