#some notes on Chapter 5
my_bool = True
print(my_bool)
my_bool = False
print(my_bool)

print(bool(1)) #true
print(bool(0)) #false
# Boolean can be two things like ON/OFF True/False Yes or NO

print(bool('')) #empty string

letter = "A"
print(ord("A"))
print(ord("B"))
print(letter < "B")

x = 10
y = 10
z = 20

print(x == 10 and y == 10)
print(x == 10 or y == 10)

x = 8
y = 9
print(x == y)
print(x != y)
print(not True)

#if BOOLEAN OR BOOLEAN EXP:
    #code block
    #for if true
#else:
    # for the if false code block

height = 75

#Must be 5 feet tall to ride my ride
#Must be under 6 feet tall to ride

if height < 60:
    print("You are too short!")
    print("I am sorry but get off of my ride!")
elif height > 72:
    print("You are too tall!")
    print("Get off my ride!")
else:
    print("Enjoy the ride!")




