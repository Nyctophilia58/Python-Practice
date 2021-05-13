# Here i'm gonna work with dictionaries
alien_0 = {'colors': 'green', 'point': 5}
print(alien_0['colors'])
print(f"You've earned {alien_0['point']} points")
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.\n")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
# If the 2nd argument doesn't exist the program will print none
print(point_value)
for key, value in alien_0.items():    # to only find keys use .keys(), to find only value  use .value()
    # or just an ordinary for loop
    print(f"\nkey : {key}\nValue : {value}")

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    new_alien['position'] = 2

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

users = {
    'a_einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'm_curie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
