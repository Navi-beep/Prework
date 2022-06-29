sandwich_orders = ['pastrami', 'tuna','pastrami', 'meatball', 'pastrami']
finished_sandwiches = []

print("\nThe deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made!")