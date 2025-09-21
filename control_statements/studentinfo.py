student_id = input("enter your id: ")
student_name = input("enter your name: ")
student_attendence = int(input("enter your attendence: "))

tota_score = 0
no_of_scoers = 0

continue_input = "yes"

while continue_input == "yes":
    current_score = int(input(f"enter score : {no_of_scoers + 1}"))
    continue_input = input("do you want to continue? (yes/no)")
    no_of_scoers +=1
    tota_score += current_score 

avg_score = tota_score/ no_of_scoers

#grading
if avg_score >= 91:
    print ("A1")
elif avg_score >= 81:
    print("A2")
elif avg_score >= 71:
    print("B1")
elif avg_score >= 61:
    print("B2")
elif avg_score >= 51:
    print("C1")
elif avg_score >= 41:
    print("C2")
elif avg_score >= 35:
    print("D1")
else:
    print("your dumbass failed HAHAHAHA")

#attendence

attendence = "KEEP YOUR ASS MORE IN CLASS" if student_attendence < 75 else "YOU GUCCI"

#award shii
if avg_score >= 85 and student_attendence > 80:
    print ("you a god fearing child")

print ("student name: " + student_name)
print (f"student total score:  {tota_score}")
print(f"average score:  {avg_score}")
print("attendence: " + attendence)