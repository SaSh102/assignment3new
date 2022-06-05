
n = int(input("Please enter the number: "))

b = n//2

m = n%2
if m == 0:
    print(b*"*#")
else:
    print(b*"*#"+"*")