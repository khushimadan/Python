def cal(n):
  k=1
  for i in range(1,n+1):
    for j in range(1,k+1):
      print("*",end="")
    k+=1
    print("\n")

n=int(input("Enter no. of lines"))
cal(n)
