'''Write a program to check whether number entered by the user is one digit, two digit or three digit number'''

num=int(input("Enter a number:"))
if num>=0 and num<10:
  print(num,"is a one digit number")
elif num>=10 and num<100:
  print(num,"is a two digit number")
elif num>=100 and num<1000:
  print(num,"is a three digit number")
else:
  print("You entered more than 3 digits")
