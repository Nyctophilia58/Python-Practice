# Here we're doing some work with functions
def make_shirt(size='large', message='I love python'):
    print(f"\nThe size of the shirt is {size}\n{message}\n")


i = 1
while i <= 3:
    shirt_size = input("What is the size of your shirt?\n")
    A_message = input("Print a message\n")
    make_shirt(shirt_size, A_message)
    i = i + 1


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}".title()
    else:
        full_name = f"{first_name} {last_name}".title()
    return full_name


i = 1
j = input("How many times do you want the loop to be executed?\nAns: ")
while i <= int(j):
    prompt = "What is your first name?\n"
    name = input(prompt)
    surname = input("Tell us your surname\n")
    print(f"Hey {get_formatted_name(name, surname)}")
    i = i+1


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
from Practice import build_profile as bp
bp('Homiya', 'Nowshin', location='Gazipur', Sex='Female')
