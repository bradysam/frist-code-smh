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
    elif select == "2":
        print("updating existing employee")
    elif select == "3":
        print("deleting current employee")
    elif select == "4":
        print("listing employee")
    elif select == "5":
        print("exit")
        break
    else:
        print("invalid option selected, please select from 1-5")