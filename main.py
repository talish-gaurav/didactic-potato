num = int(input("Enter your number"))

if num%20 == 0:
    print("twist")
elif num%15 == 0:
    pass
elif num%5==0:
    print("buzz")
else:
    print(num)