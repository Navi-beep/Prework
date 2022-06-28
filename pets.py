pets = []

animal_0 = {
    'owner': 'robert', 
    'pet_type': 'iguana',
    'name': 'rupert',
    'eats': 'pop-tarts'
}
pets.append(animal_0)

animal_1 = {
    'owner': 'elise', 
    'pet_type': 'cockatiel',
    'name': 'peanut',
    'eats': 'sunflower seeds'
}
pets.append(animal_1)

animal_2 = {
    'owner': 'natalie', 
    'pet_type': 'tiger',
    'name': 'dimitri',
    'eats': 'steak'
}
pets.append(animal_2)

print(pets)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

    
