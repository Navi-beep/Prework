bird = 'cockatiel'
print("Is bird == 'cockatiel'? I predict True")
print(bird == 'cockatiel')
print("\nIs bird == 'parakeet'? I predict False.")
print(bird =='parakeet')

if bird != 'canary':
    print("I did not want a canary!")
if bird == 'cockatiel':
    print("I want a cockatiel from the pet store!")

cat = 'tuxedo'
print("Is cat == 'tuxedo'? I will predict True.")
print(cat == 'tuxedo')
print("\nIs cat == 'shorthair'? I will predict False.")
print(cat =='shorthair')

dog = 'pug'
print("Is dog == 'pug'? I predict True")
print(dog == 'pug')
print("\nIs dog == 'doberman'? I predict False.")
print(dog =='doberman')

bird = 'budgie'
print("Is bird == 'budgie'? I predict True")
print(bird == 'budgie')
print("\nIs bird == 'finch'? I predict False.")
print(bird =='finch')

number = 2
print("Is number == '2'? I predict True")
print(number == '2')
print("\nIs number == '3'? I predict False.")
print(number =='3')

birb = 'Eagle'
birb.lower() == "eagle"
print(birb == 'Eagle')

cat = 'Longhair'
birb.lower() == "longhair"
print(cat == 'Longhair')

answer = 20
if answer != 45:
    print("That is the wrong age!, please guess again!")
if answer == 20:
    print("You guessed correctly")
if answer >= 15:
    print("That is correct!")
if answer <= 30:
    print("That is not correct!")

age_0 = 25
age_1 = 15
print(age_0 == 25)
print(age_1 == 15)
if age_0 == 25: print(age_0)
print(age_0 <= 30 or age_1 >=10)
print(age_0 >= 30 and age_1 <=10)

animal_list = ['iguana','hamster','parrot','frog']
animal = 'hamster'
animal_1 = 'jackel'
if animal in animal_list: print(True)
if animal_1 not in animal_list: print(False)
