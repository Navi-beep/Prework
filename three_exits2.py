prompt = "\nWhat would you like on your pizza?:"

active = True
while active:
    pizza = input(prompt)
    if pizza == 'quit':
        active = False
    else: 
        print(f"I will add {pizza} topping to your pizza!")