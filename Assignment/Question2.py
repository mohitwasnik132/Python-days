
# Solution For given Assignment Q.2
for row  in range(5):
  for col in range(5):
    if (row+col==2 or col-row==2 or row-col==2 or row+col== 6 ):
      print("@ ",end="")
    else:
      print(end="# ",)
  print()

print("\n\n")



# Modified For user input
size = int(input("Enter size: "))
diamond = input("Specify symbol/pattern for inner diamond: ")
fill = input("Specify the grid fill symbol(Space for empty): ")

print (f"The grid of size {size}x{size} with\ninner {diamond} diamond\nFill of {fill} looks like below:\n ")
size=size+1

# For odd numbers
if size%2==0 :
 size = size-1
 center = int((size/2))
else:
 center = int((size/2))


final_size = (center + size) -  1



for row in range(size):
  for col in range(size):
    if (row+col==center or col-row==center or row-col==center or row+col==center  or row+col==final_size):
      print(f"{diamond} " ,end="")
    else:
      print(f"{fill} ",end="")
  print()



