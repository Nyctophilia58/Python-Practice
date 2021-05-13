# In this program we're gonna try some simple math programs using python
A = input("Pick a number \"A\"\n")
B = input("Pick a number \"B\"\n")
print("The summation of A and B is", str(int(A)+int(B)))
if A > B:
    print("A is bigger than B so the subtraction of A and B is", str(int(A)-int(B)))
elif A == B:
    print("A is equal to B so the subtraction of A and B is 0")
    print("Yay the numbers are equal:)")
else:
    print("A is lesser than B so the subtraction of B and A is", str(int(B)-int(A)))

print("The multiplication of A and B is", str(int(A)*int(B)))
print("The division of A and B is", str(int(A)/int(B)))
print("The modulation of A and B is", str(int(A) % int(B)))

# gonna use ** to exponents
print(A, "multiplied", B, "times = ", int(A) ** int(B))

