name_prompt = "\nWhat's your name? "
destination_prompt = "What would be your dream vacation destination? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    destination = input(destination_prompt)
    responses[name] = destination

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")