'''Write a menu driven script to calculate the total surface area and volume of a cube, cuboid, or sphere depending upon user’s choice'''

print("Choose a number for calculating Tsa and Volume")
print("Enter 1 for cube")
print("Enter 2 for cuboid")
print("Enter 3 for sphere")
x=int(input("Enter:"))
if x==1:
  y=int(input("Enter the side"))
volume=y**3
  tsa=(y**2)*6
  print("Volume of cube is",volume)
  print("TSA is",tsa)
elif x==2:
  m=int(input("Enter length"))
  l=int(input("Enter breadth"))
  k=int(input("Enter height"))
  TSA=2*(m+l+k)
  vol=m*l*k
  print("Volume of cuboid is",vol)
  print("TSA is",TSA)
elif x==3:
  r=int(input("Enter radius"))
  volu=4/3*22/7*r**3
  sa=4*22/7*r**2
  print("Volume of sphere is",volu)
  print("TSA is",sa)
else:
  print("Invalid input")
