favorite_places = {
    'dan': ['hawaii', 'canada'],
    'elise' : ['tokyo', 'cairo', 'vancover'],
    'jeff': ['chicago', 'milwaukee']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")