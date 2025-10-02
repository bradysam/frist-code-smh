print("."*50)
print("            STUDENT INFORMATION")
print("."*50)

stu_id_valid = False

while not stu_id_valid:
    stud_id = input("Enter your ID: ")
    if stud_id.startswith("-") and stud_id[1:].isdigit():
        print("enter a valid id")
    elif stud_id.isdigit():
        stud_id = int(stud_id)
        if stud_id > 0:
            stu_id_valid = True
        else:
            print("Srudent ID can NOT be ZERO")
    else:
        print("enter a valid Student ID")
else:
    print("student ID:",stud_id)