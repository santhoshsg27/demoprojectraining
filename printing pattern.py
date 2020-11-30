'''for i in range(4):
    for j in range(4):
        print('#', end=" ")
    print()'''
'''for i in range(1):
    a = " #"
    j = 1
    while j <= 4:
        print(a*j)
        j += 1
    print()'''
'''for i in range(4):
    for j in range(i+1):
        print('#', end=" ")
    print()'''
'''for i in range(1):
    a = " #"
    j = 4
    while j >= 1:
        print(a*j)
        j -= 1
    print()'''
for i in range(4):
    for j in range(4-i):
        print('#', end=" ")
    print()
