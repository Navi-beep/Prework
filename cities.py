cities = {
    'chicago': {
        'country': 'united states',
        'population': 2690000,
        'state_bird': 'northern cardinal',
        },
    'milwaukee': {
        'country': 'united states',
        'population': 600000,
        'state_bird': 'american robin',
        },
    'salem': {
        'country': 'united states',
        'population': 43350,
        'state_bird': 'chickadee',
        }
    }

for location, location_info in cities.items():
    country = location_info['country'].title()
    population = location_info['population']
    bird = location_info['state_bird'].title()

    print("\n" + location.title() + " is in the " + country + ".")
    print("  It has a population of " + str(population) + ".")
    print("The " + bird + " is the offical state bird.")

