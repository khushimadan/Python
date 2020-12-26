#WAP to display N armstrong numbers. Use user defined function.

def armstrong(a):
  j=1
  num=1
  while j<=n:
    sum=0
    a=num
    while num!=0:
      d=num%10
      d=d**3
      sum+=d
      num//=10
    if sum==a:
      print(a)
      j+=1
    num=a+1

n=int(input("Enter the no. of armstrong no's:"))
print(armstrong(n))
