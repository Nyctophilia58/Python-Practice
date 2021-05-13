# In this program we're gonna play with string

my_string = input("Input a quote\n")
print(my_string.title() + "\n" + my_string.upper() + "\n" + my_string.lower() + "\n" + str(my_string.islower()))
# (.title means the input quote will be presented as a title)
# (.lower means the input quote will be presented as a string of lower case)
# (.upper means the input quote will be presented as a string of upper case)
# (.isupper means if the input quote is a string of upper case then True value will be presented otherwise False)
# (.isupper means if the input quote is a string of lower case then True value will be presented otherwise False)
# we can also use .upper().isupper(), it'll print out True same goes for .lower().islower()

# Now we're gonna work with "Placeholders"
first_name = input("What is you first name?\n")
last_name = input("What is your last name?\n")
full_name = "So your name is {}"
full_name = full_name.format(first_name + " " + last_name)
print(full_name.title())

# another way to use placeholders
full_name = "So your full name is {}".format(first_name + " " + last_name)
print(full_name.upper())

# another way to use placeholders
print("So your full name is {}".format(first_name + " " + last_name).lower())

# another way to use placeholders
full_name = f"So your name is {first_name} {last_name}"
print(full_name.upper())

# another way to use placeholders
print(f"So your name is {first_name} {last_name}".lower())

# Stripping whitespace
fav_language = input("What is your favorite language?\n")
print(fav_language.rstrip())   # r.strip means the useless space on the right of a string disappears
print(fav_language.lstrip())   # l.strip means the useless space on the left of a string disappears
print(fav_language.strip())    # strip means all the useless spaces on right or left of a string disappears

# Using apostrophe comma
# Here \t doesn't work but \n works
print("\tOne of python's best feature is that it can identify\napostrophe comma\t".strip())

# replace function
quote = "Live while you're alive"
print(quote.replace("Live", "Bloom"))

# index function
print(quote.index("while"))
my_num = -3
absolute = abs(my_num)  # absolute value
power = pow(my_num, abs(my_num))    # power
print("Maximum number is", max(absolute, power), "Minimum number is", min(absolute, power))
num = 3.2
print(round(num))
num = 3.8
print(round(num))   # floor(), ceil(), sqrt()--->>from math import
