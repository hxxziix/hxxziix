
n = int(input())

for i in range(1, n+1) :

    for a in range(n-i) :
        print(" ", end = "")

    for b in range(i) :
        print("*", end = "")
    
    print()