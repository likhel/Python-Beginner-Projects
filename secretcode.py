def listtostrings(s):
 str1=" "
 return(str1.join(s))

print("if you want to code press C")
print("if you want to decode press D")

x=input("Do you want to code or decode:(C/D)")


if x=='C' or x=='c': 
 string=input("Enter a word to code into secret language:")
 if len(string)>3:
  hello=[i for i in string]
  print(hello)
  hello.append(hello[0])
  print(hello)
  hello.remove(hello[0])
  hi=listtostrings(hello)
  print(hi)
  beg=input("enter a two word to add at first:")
  end=input("enter a two word to append at last:")
  if len(beg)==2 and len(end)==2:
   reverse=beg+hi+end
   print(reverse[::-1])
  else:
   raise ValueError("Entered letters are too long....")

 else:
  string1=string[::-1]
  print(string1)

elif x=='D' or x=='d':
 word=input("Enter a secret language word to decode: ")
 if len(word)<=3 :
  print("The decoded word is:",word[::-1])
 else:
  word3=word[::-1]
  word1=[i for i in word3]
  print(word1)
  
  word1.remove(word1[0])
  word1.remove(word1[0])
  word1.remove(word1[len(word1)-1])
  word1.remove(word1[len(word1)-1])
  print(word1)
  word4=word1[len(word1)-1]
  result1=word4
  result=[result1]
  result2=result+word1
  print(result2)
  result2.pop(len(result2)-1)
  print(result2)
  word2=listtostrings(result2)
  print(word2)

else:
 print("Invalid input.....")
  
  
  
 
 



  
