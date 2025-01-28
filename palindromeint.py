def pal(n):
    number = n
    reverse_num = 0
    list1 = []
    list2 = []

    while number>0:
        remainder = number%10
        list1.append(remainder)
        #reverse_num = (reverse_num*10)+remainder
        number = number//10
    list2 = [str(i) for i in list1]
    reverse_num = int("".join(list2))
    print(reverse_num)
    if n == reverse_num:
        return f"{reverse_num} is a palindrome"
    else:

        return f"{reverse_num} is not a palindrome"


y = pal(1551)
print(y)
    
