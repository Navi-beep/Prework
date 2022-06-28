people = []

person = {'first_name': 'Bill', 'last_name': 'Nye', 'age': 66, 'location': 'Los Angeles'}

people.append(person)

person = {'first_name': 'Phil', 'last_name': 'Gopher', 'age': 33, 'location': 'Punxsutawney'}

people.append(person)

person = {'first_name': 'Michel', 'last_name': 'Scott', 'age': 43, 'location': 'Scranton'}

people.append(person)
print(people)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    location = person['location'].title()

    print(name + ", who resides in " + location + ", is " + age +".")
