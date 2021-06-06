n=int(input("Enter range="))
i=0
first=0
second=1
while(i<=n):
  if(i<=1):
    Next=i
  else:
    Next=first+second
    first=second
    second=Next
  print(Next)
  i+=1
