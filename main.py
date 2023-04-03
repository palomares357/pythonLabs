# oscar j palomares
# main.py
# program that will accept student names and GPAs
# and test if the student qualifies for either the Dean's List or the Honor Rol


firstName = ""
gpa = 0

while True:
    lastName = input("Please input your last name: ")

    if lastName == "ZZZ":
        break

    else:
        firstName = input("Please input your first name: ")
        gpa = float(input("Please input your GPA: "))
        break

if gpa >= 3.5:
    print(firstName.capitalize() + " " + lastName.capitalize() + " has made the Dean's List.")
elif gpa >= 3.25:
    print(firstName.capitalize() + " " + lastName.capitalize() + " has made the Honor Roll.")
else:
    print("")
