# This is a simple program
print("Hello World, this is my first python program\n"
      "I am a noob,but hopefully i'm gonna have a good time learning python\n")

# Learning about variables
name = "Nowshin"
age = "20"
print("My name is", name, "and my age is", age)

# another way to input variable
name = input()
age = input()       # here the age gets input as a string so i can put any int or float value it shouldn't matter
print("My name is", name, "and my age is", age)

# another way to input variable
name = input("What is your name?\n")
age = input("What is your age?\n")
print("My name is", name, "and my age is", age)

# another way to input variable
name, age = input("What is your name?\n"), input("What is your age?\n")
print("My name is", name, "and my age is", age)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
