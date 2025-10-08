SYSTEM_INFO = ("Sheepy's Fold", "Employee Database", "v1")
ADMIN_INFO = ("0123456789","sheepysfold@interiordesign.com")
employee = {}

while True:
    print("choose an option:")
    print("1-add employee")
    print("2-update employee")
    print("3-delete employee")
    print("4-list employees")
    print("5-exit system")

    select = input("select an option(1-5):")

    if select == "1":
        print("adding employee")
        employee_id = input("enter employee id:")
        if employee_id in employee:
            print("id already exists")
        else:
            name = input("enter name:").title()

            working_hrs = []
            while True:
                wrkhrs = input("enter your working hrs:")
                if wrkhrs == "done":
                    break
                if wrkhrs.isdigit():
                    hour = int(wrkhrs)
                    if 0 <= hour <= 24:
                        working_hrs.append(wrkhrs)
                    else:
                        print("invalid working hrs")
                else:
                    print("should be numbers only")
            #set for skills
            skills = set()
            while True:
                skillsin = input("enter your skills:")
                if skillsin == "done":
                    break
                skills.add(skillsin.title())
            #save the details 
            employee[employee_id] = {
                "name": name,
                "working hours": working_hrs,
                "skills": skills
            }
            print("employee saved")
            print(employee)

    elif select == "2":
        print("updating existing employee")
        employee_id = input("enter employee id to update:")
        if employee_id in employee:
            new_name = input("enter name:").title()
            employee[employee_id]["name"] = new_name
            print("name updated")
        else:
            print("id does not exist")
        print(employee)


    elif select == "3":
        print("deleting current employee")
        employee_id = input("enter employee id to delete:")
        if employee_id in employee:
            delete = employee.pop(employee_id)
            print(delete)
        else:
            print("id does not exist")
        print(employee)


    elif select == "4":
        print("listing employee")
        for eid, data in employee.items():
            name = data["name"]
            working_hrs = data["working hours"]
           
            avg = sum(working_hrs)/ len(working_hrs)
            highest = max(working_hrs)
            lowest = min(working_hrs)

            skills = data["skills"]
            skillcou = len(skills)
            print("*"*50)
            print("EMPLOYEE DETAILS")
            print("*"*50)

            print(f"ID:{eid}")
            print(f"NAME:{name}")
            print(f"WORKING HOURS:{working_hrs}")
            print(f"AVERAGE WORK HOURS:{avg}")
            print(f"MAXIMUM HOURS WORKED:{highest}")
            print(f"LOWEST HOURS WORKED:{lowest}")
            print(f"ALL SKILLS:{skills}")
            print(f"NUMBER OF SKILLS:{skillcou}")
            
    elif select == "5":
        print("exit")
        print("*"*50)
        print("CONTACT ADMIN FOR MORE INFO")
        print(f"ADMIN CONTACT:{ADMIN_INFO}")
        print("*"*50)
        break
    else:
        print("invalid option selected, please select from 1-5")