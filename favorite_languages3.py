favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'bob': 'c++',
    'susie': 'javascript',
    'jeff': 'c#'
    }

friends = {
        'robert': 'x',
        'ted': 'x',
        'bill': 'x'
    }
 
for name in (favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

for name in (friends.keys()):
    print(f"{name.title()}, Please take the poll!")