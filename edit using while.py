sandwich_orders = ['apple','banana','egg']
finished_sandwiches = []
while sandwich_orders:
    sos = sandwich_orders.pop()
    finished_sandwiches.append(sos)
print("\nlisting each sandwich that was made.")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())