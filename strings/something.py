sou_email = input("enter your email id: ")
desti_email = input("enter your email id: ")
if sou_email.endswith ("@gmail.com") and desti_email.endswith ("@gmail.com"):
    print("email correct")
else: 
    print("check your email you dounut")

emprow = "brady, blr, 21, sheeepy@gmail.com"
print("original data: "+ emprow)
field = emprow.split(",")
print(field)

print("name: "+field[0])
print("age: "+field[2])

#order id replace
ordertemp = "hellp, your order #{order id} has been shipped"
orderid = "NIBRA-1908-IN"

uderem = ordertemp.replace("order id", orderid)
print(uderem)