age = input("How old are you?")
age = int(age)

if age <= 3:
    print("\nYou're ticket is free!")

elif age <= 12:
    print("\nYou're ticket is $10!")

else:
    print("\nYour ticket is $15!")