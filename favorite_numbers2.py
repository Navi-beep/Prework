favorite_numbers = {
    'carrie': [5,12],
    'ted': [17,35,62],
    'jonathan': [32,13,4],
    'leahy': [64, 555],
    'randy': [128, 56]
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")