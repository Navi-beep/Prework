names = ['natalie', 'ken', 'abraham lincoln', 'david bowie']
print(f"Hello, {names[0].title()}, {names[1].title()}, {names[2].title()}, and {names[3].title()}, we found a bigger dinner table!")

names.insert(0, 'kiwi')
names.insert(2, 'ted')
names.insert(3, 'yuki')
print(names)

message1 = f"Hello {names[0].title()} you are invited to dinner!"
print(message1)

message2 = f"Hello {names[1].title()} you are invited to dinner!"
print(message2)

message3 = f"Hello {names[2].title()} you are invited to di(nner!"
print(message3)

message4 = f"Hello {names[3].title()} you are invited to dinner!"
print(message4)

message5 = f"Hello {names[4].title()} you are invited to dinner!"
print(message5)

message6 = f"Hello {names[5].title()} you are invited to dinner!"
print(message6)

message7 = f"Hello {names[6].title()} you are invited to dinner!"
print(message7)

print(f"Hi everyone, now I can only invite two guests to dinner.")

last_guest = names.pop()
print(f"Sorry, {last_guest.title()} I cannot invite you to dinner.")

last_guest = names.pop()
print(f"Sorry, {last_guest.title()} I cannot invite you to dinner.")

last_guest = names.pop()
print(f"Sorry, {last_guest.title()} I cannot invite you to dinner.")

last_guest = names.pop()
print(f"Sorry, {last_guest.title()} I cannot invite you to dinner.")

last_guest = names.pop()
print(f"Sorry, {last_guest.title()} I cannot invite you to dinner.")

del names[0]
print(names)

del names[0]
print(names)
