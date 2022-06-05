import array

a_array=[]
lst=[]
while True:
    x=int(input("Enter a number or -1 to exit: "))
    if x == -1:
        break
    else:
        a_array.append(x)
        
      
print(a_array)
lst = a_array.copy()

def BubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst
print(BubbleSort(lst))


if lst == a_array:
    print("OK 🙂")
else:
    print("NO 😮")


