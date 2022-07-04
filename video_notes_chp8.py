# def Name_of_function(parameters):
    # these lines
    #belong 
    #to the code block
    # for the function
    
#return - will make the value of the function executed i.e. hello() the object that is returned from the function. 

# it is like saying hello() = "hello"

# python functions returns None by default 

def say_hello(name, age):
    print(f"Hello {name.title()}, you are {age} years old")

def say_goodbye():
    print("Goodbye")

def greet_back(feeling):
    if feeling == "good":
        print("Awesome, I feel good too")
    elif feeling == "bad":
        print("I am so sorry")
    elif feeling == "stressed":
        print("Coding can be hard to learn")
    else:
        print("Well, have a good day!")

# Driver code
while True:
    response = input("What do you want to do? Say hello [H] Say Goodbye [G] talk to me [T], quit [Q]")
    if response.lower() == 'q':
        say_goodbye()
        break
    elif response.lower() == 'h':
        name = input("What is your name?")
        age = input("what is your age?")
        say_hello(name,age)
    elif response.lower() == 'g':
        say_goodbye()
    elif response.lower() == 't':
        feeling = input("How are you today?")
        greet_back(feeling)
    else:
        print("invalid input")

def my_function(num):
    while num < 10:
        print(num)
        if num == 6:
            return
        num +=1

my_function(4)

