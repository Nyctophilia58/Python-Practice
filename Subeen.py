# Problem number 3
"""i = 1000
while i != 0:
    print(f"{i}\t{i-1}\t{i-2}\t{i-3}\t{i-4}")
    i = i-5"""

# Problem 4
T = input()
for i in range(1, int(T)+1):
    N = input()
    for j in range(1, int(N)+1):
        if N % j == 0:
            print(j)
