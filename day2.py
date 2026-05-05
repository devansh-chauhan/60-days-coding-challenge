marks = int(input("Enter your marks:"))
if marks < 0 or marks > 100:
    print("Invalid input! Please enter marks between 0 and 100.")
else:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")


    if marks >= 50:
        print("Status: Passed")
    else:
        print("Status: Failed")