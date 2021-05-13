# For loop
pizzas = ['Pepperoni', 'Cheesy', 'Cucumber']
for pizza in pizzas:
    print(pizza)
print("I really love pizza")
for i in range(1, 5):
    print(i)
String = [i for i in range(1, 5)]
print(String)
s = []
for i in range(1, 5):
    st = i ** 2
    s.append(st)    # or s.append(i ** 2)

print(s)
print("The summation is", sum(s), "\nminimum number is", min(s), "\nmaximum number is", max(s))
print(s[0:2])
print(s[:-1])    # starts from the beginning of the list
print(s[-2:])    # prints till the last element of the list
print(s[::2])

# While loop
i = 5
while 1:
    print("What?")
    i = i-1
    if i == 0:
        break
