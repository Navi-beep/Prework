pizzas = ['cheese', 'pepperoni', 'sausage']
friend_pizzas = pizzas[:]

pizzas.append('vegetable')
friend_pizzas.append('greek')

print("My favorite pizzas are:")
for pizza in pizzas: 
        print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
        print(friend_pizza)
