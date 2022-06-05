import random
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
word = random.choice(words)
joon = 10

print("_ " * len(word))
c=0
for letter in word:
    c+=1
x=c*"_"

n=list(x)

while joon > 0:
    user_char=input("Yek Harf Vared Konid: ")
    user_character=user_char.lower()
    x2 = ''
    while "_" in n:
        x2 = ''
        if user_character in word:
            for z in range(0 , len(word)):
                if word[z]==user_character:
                    n[z]=word[z]
                x2 = x2 + n[z]
            print(x2)
            if "_" in n:
                user_char=input("Affarin. Yek Harf Dighar Vared Konid: ")
                user_character = user_char.lower() 
        
            else:
                if user_character in word:
                    print('yes😍💪')
                    break
                
        else:
            joon = joon - 1
            print('no')
            user_char=input("Eshtebah Ghoftid. Yek Harf Dighar Vared Konid: ")
            user_character=user_char.lower()
    
            if joon == 0:
                print("Moteasefane Bakhti😭😭")
                break
