n = int(input("Enter the number : "))
for i in range (n,0,-1):
    print(" " * ((n - i) * 1), end ="")
    val = n-i+1
    for j in range(i):
        print(val, end=" ")
        val = (val+i-j)+(n-i)
    print("")
