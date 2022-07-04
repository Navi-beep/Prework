def sandwich(*ingredients):
    """"Print a list of sandwich ingredients that have been requested"""
    print("\nMaking a sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f"- {ingredient}")


sandwich('tuna', 'mayo')
sandwich('bologna', 'salami', 'mayo')
sandwich('peanut butter', 'jelly', 'butter', 'banana')