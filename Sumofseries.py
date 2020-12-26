'''WAP to calculate the sum of the series
1-x2/4!+x3/6!-x4/8!+x5/10!......xn/(2n)!
Accept the values of x and n from the user and pass them to a function to return the sum of the series.'''

def sum(n,x):
  k=2
  sum=1
  while k<=n:
fact=1
    for i in range(1,(2*k)+1):
      fact=fact*i
    term=(x**k)/fact
    if(n%2==0):
      sum-=term
    else:
      sum+=term
    k+=1
  print("Sum of series=",sum)

n=int(input("Enter limit:"))
x=int(input("Enter your number:"))
sum(n,x)
