# Starting to learn about lists
bicycles = ['trek', 'cannondel', 'redline', 'specialized']
print(bicycles)     # Here string methods doesn't work
print(bicycles[-3].title())    # Here - index means the array element from last
# (-1 = last element of array,-2 = 2nd last element and so forth)

print(f"I would love to ride {bicycles[2]}")
names = ['Nowrin', 'Tanisha', 'Sumi', 'Akhi']
for i in names:    # range(length) = names
    print("You are my friend", i)    # f"you're my friend,{names[i]}"

names.append('Jonak')  # It inserts an extra in ip/kb dex and puts the element there
names.insert(2, 'Tinne')  # It inserts an extra index by users choice and puts the element there
del names[4]    # Here we delete the given indexed element
popped_name = names.pop()    # i can also use index number inside pop to pop out any element i want
print(names.pop(0))
names.remove('Tinne')    # This helps if i don't know the index number which i want to remove
# it only removes the element one time so if the element appears more than once then i would've to use loop
print(names)
print(popped_name)

# I can also merge the elements together
Count = ['1', 'three', 'six', 'four'+'three', 'two']   # here four and three would merge together and produce fourthree
print(Count)
Count = [1, 2, 3, 4]
print(Count)
Count.extend(names)
print(Count)    # insert, clear, index, count
