if 5 > 2:
    print("correct")
if True:
    print ("you a btixh")
    print("dumbo")
print ("this mf playin too much")

num = 96
if ( num > 0):
    print("lightningMqueen")

bro = 20
if (10<= bro <= 20):
    print("bro is legal")

dude = 25
if ( dude >= 18):
    print("dude is chilling")
else:
    print("pedo")

#input () :
name = input("enter your name:")
print("hello:"+name)
age = int(input("enter your age:"))
gender = input("enter gender:")
if (age>=21):
    print("you are allowed to drink")
if (age>35):
    print("welcome unc")
else:
    print("go home")

#ternary operator 
name = input("enter your name:")
age = int(input("enter your age:"))
stats = "you can enter" if age>=21 else "get out"
print(stats)


#elif ladder 
speed = int(input("speed caught at:"))
if speed <= 50:
    print ("impeeding traffic")
elif speed >=200:
    print ("dangerous driving")
elif speed >= 180:
    print ("rash driving")
elif speed >= 150:
    print ("speeding")
elif speed >= 120:
    print ("negligant driving")
elif speed >= 80:
    print ("appropriate speed")