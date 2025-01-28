list1 = [4,5,1,2,3]

def  sort(l1):
    n = len(l1)

    for i in range(n):
        for j in range(n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j]

    print(l1)

sort(list1)
