def build_profile(first, last, **user_info):
    """Building my own profile"""
    user_info['First_name'] = first
    user_info['Last_name'] = last
    print(user_info)


owners = ['patric', 'sofia', 'killian', 'josey']
dogs = ['australian', 'poodles', 'bulldog', 'chuyala']
print(list(zip(owners, dogs)))


def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()


def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()


def coffee_bot():
    print('Welcome to the cafe!')
    order_drink = 'y'
    drinks = []
    while order_drink == 'y':
        size = get_size()
        drink_type = get_drink_type()

        drink = f"{size} {drink_type}"
        print(f"Alright, that's a {drink}!")
        drinks.append(drink)
        while True:
            order_drink = input("Would you like to order another drink? (y/n) \n>")
            if order_drink in ['y', 'n']:
                break

    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your order will be ready shortly.'.format(name))


def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return order_mocha()
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()


# Define new functions here!

def order_mocha():
    while True:
        res = input(
            "Would you like to try our limited-edition peppermint mocha?\n[a] Sure! \n[b] Maybe next time! \n> ")
        if res == 'a':
            return 'peppermint mocha'
        elif res == 'b':
            return 'mocha'

        print_message()


coffee_bot()

print("So i have: ")
for i in drinks:
    print(i, "\n")




class Employee:

    raise_amount = 1.04

    def __init__(self, last, pay, first="Homiya"):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@gmail.com"
        self.pay = pay
        self.is_moving = False

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def stop(self):
        if self.is_moving:
            print(f"{self.first} has stopped")
            self.is_moving = False
        else:
            print(f"{self.first} has already stopped")

    def go(self, speed):
        if not self.is_moving:
            print(f"{self.first} starts moving")
            self.is_moving = True
        print(f"{self.first} is going {speed}")


emp_1 = Employee('Nowshin', 50000)
emp_2 = Employee('Tasnim', 60000, 'Anindita')

print(emp_1.full_name())
print(Employee.full_name(emp_2))
emp_1.stop()
emp_2.go('slow')
emp_2.go('fast')
emp_1.stop()
emp_1.stop()

print(dir(emp_1))


