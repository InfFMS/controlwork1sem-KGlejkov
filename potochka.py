b='' 
for x in range (1, 2031): 
  a=3**100-x
  while a>0:
    b=str(a%3) + str(b)
    a=a//3
  if b.count('0')==2:

    print (x)

    break
  b=''
