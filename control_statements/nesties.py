age = int(input("please enter your age:"))
identi = input("do you consume alcohol?(yes/no):")

if age <18:
    print ("no booze for you")

if 21 >= age >= 18:
    if identi == "yes":
        print("you need your parents with you")
    else:
        print("no drinks for you")
if age >= 21:
    if identi =="yes":
         print("enjoy your evening")
    else:
        print("no drinks for you")

#for nested loops
for row in range(25,30):
    for column in range(25,30):
        print(f"{row} x {column} = {row*column}")
    print("**************")

