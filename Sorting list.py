# I'm gonna sort the list elements
Count = ['one', 'three', 'six', 'four'+'three']
Count.sort()
print(Count)    # here print(count.sort()) doesn't work. It replies with the message "None"

Count = [5, 'two', '3', 100, 'thirty']
print(Count)

Count = [5, 7, 3, 4, 2]
Count2 = Count.copy()
print(Count2)
length = len(Count)
print("The length of the list named count is "+str(int(length)))
Count.sort()
print(Count)
Count.sort(reverse=True)  # it makes the list reverse
print(Count)
print("The 3rd last element of the list is", Count[-3])

# Sorted() function
Something = ['1', 'one', '4', '2', 'four', '10', 'Ten']
print(sorted(Something))    # alphabetically sorts the list but doesn't change the list. It also works on strings
print(sorted(Something, reverse=True))    # a way to reverse the list with sorted function without actually reversing it
print(Something)
Something.reverse()    # just reverses the list(not alphabetically)
print(Something)    # here print(something.reverse()) doesn't work. It replies with the message "None"
