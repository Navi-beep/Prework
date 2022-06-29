prompt = "\nWhat would you like on your pizza?:"

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else: 
        print(f"I will add {pizza} topping to your pizza!")