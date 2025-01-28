def count(words):
    n = len(words)
    count1 = 0
    count2 = 0
    list1 = []
    list2 = []
    for  i in words:
        if i.isupper():
            count1 += 1
            list1.append(i)

        elif i.islower():
            count2 +=1
            list2.append(i)
        
        else:
            print("enter alphabet")
        
    
    print(f"the numbers of uppercase letters are {count1} and the number of lowercase letters are {count2}")
    print(f"the uppercase and lowercase words are: {''.join(list1)} and {''.join(list2)}")

name = input("enter your name:")
print(name)
count(name)






