print("Grading System, Enter the marks for the following subjects:")
math = int(input("1. Maths: "))
phyc = int(input("2. Physics: "))
geog = int(input("3. Geography: "))
chem = int(input("4. Chemistry: "))

if (math < 0 or phyc < 0 or geog < 0 or chem < 0) or (math > 100 or phyc > 100 or geog > 100 or chem > 100):
    print("Unrecognized marks/average\n")
else:
    sum = math + phyc + geog + chem
    average = sum / 4
    if 70 < average <= 100:
        grade = "A"
    elif 50 < average <= 70:
        grade = "B"
    elif 30 < average <= 50:
        grade = "C"
    else:
        grade = "D"

    print(f"Your average is:  {average} {grade}")