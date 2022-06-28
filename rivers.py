rivers = {
    'nile': 'egypt',
    'ganges':'india',
    'amazon': 'peru'
    }

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")
    print(f"\nKey: {key.title()}")
    print(f"\nValue: {value.title()}")
