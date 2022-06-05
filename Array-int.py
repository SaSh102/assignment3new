from random import randint


n=int(input("Please enter the number: "))
random_array=[]


for i in range(n):
    a= randint(0, 1000+n)
    if a not in random_array:
        random_array.append(a)
    

print(random_array)

