my_dict = {}
my_dict = dict()

my_dict = {
    "key":"value"
}

my_dict = dict(key="value")

# a dictionary is a collection of key value pairs

steve = {
    "name" : "Steve", #Str
    "weight" : 155.5, #flt
    "height": 70, #int
    "foods": ["country fried steak", "fried chicken", "collards"],
    "ice cream": {
        "vanilla": False,
        "chocolate": True,
        "coffee": False,
    },
    10 : "this has an integer key"
}
# name_of_dict[KEY]
print(steve["ice cream"]["vanilla"])
print(type(steve["ice cream"]["vanilla"]))

print(steve.get("candies")) #returns NONE if nothing there
print(steve.get("candies", "No Candy List")) # will return second argument if nothing there


my_list = [1,2,3]
my_list[1] = "WOW"
print(my_list)

# add key value pair to steve list
steve.update({"candies" : ["snickers", "mars", "m&ms"]})
print(steve)

del steve["candies"]
print(steve)


for key in steve:
    print(key)
    print(type(key))
    print(steve[key])

print(steve.values()) # loop through values
for value in steve.values():
    print(value)
    print(type(value))

print(steve.items()) #
for key , value in steve.items():
    print(key, end = " ")
    print(value)

for key , value in steve.items():
    if isinstance(value,list): #return whether an object is an instance of a class or of a subclass thereof. 
        print(f"The list is at {key}")






