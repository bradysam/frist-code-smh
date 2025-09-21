import random
otp = random.randint(1000,9999)
print(otp)
attempts = 3

while attempts :
    userotp = int(input("ENTER OTP:"))
    if len(str(userotp)) !=4:
        print("OTP must be 4 digits only")
    if userotp != otp:
        print("incorrect otp")
    if userotp == otp:
        print("Transaction success")
        break
    attempts -= 1
else:
    print("MAXIMUM attempts reched please try again after 24 hours")