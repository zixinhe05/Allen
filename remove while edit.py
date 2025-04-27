sandwich_orders = ['apple','banana','egg','pastrami','pastrami','pastrami']
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)