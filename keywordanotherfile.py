def getsinfo(*args):
   sum = 0
   fact = 1
   list = args[0]
   #args = list(args)
   for i in list:
      sum+=i

   for i in list:
      fact = fact*i

   return sum,fact
      