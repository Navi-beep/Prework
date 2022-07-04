# the variable username in the definition of greet_user() is an example of a parameter, information that the function needs to do its job

# the value 'elise' is greet_user('elise') is an example of an argument. 

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('elise')

