def right_tri(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print("*",end="")
        print("")

right_tri(5)