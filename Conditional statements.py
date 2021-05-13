# if-elif
Name = input("What is your name?\n")
if Name == "Nowshin":
    print("Hello,", Name, "Nice to meet you")
elif Name != "Nowshin":
    print("Sorry, can't process your name")
Age = input("What is you age?\n")
if int(Age) >= 18:
    print("Wow that is great. You're not a teenager now")
else:
    print("Still a teenager")
Rec_toppings = ['mushrooms', 'onions', 'pineapples']
if 'mushrooms' in Rec_toppings:
    print("I've found it")
if 'coca' not in Rec_toppings:
    print("It's not inside the list")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


# There's more
