
food = ['pizza', 'sushi', 'tacos']
print(food)
print(food[0])
print(food[1].title())
print(food[-1])
message = f"My favorite food is {food[0].title()}."
print(message)
food[1] = 'lasagna'
print(food)
food.append('bagels')
print(food)
food.insert(0, 'chicken nuggets')
print(food)
del food[0]
print(food)
popped_food = food.pop()
print(f"My second favorite food is {popped_food}.")

food.remove('tacos')
print(food)

print(sorted(food))
print(sorted(food, reverse=True))
food.sort()
print(food)
food.reverse()
print(food)
print(len(food))


