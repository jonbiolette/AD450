def compute_GPA(percent):
    if (percent <= 100 and percent > 0):
        if (percent <= 100 and percent >= 95):
            return ("4.0")
        elif (percent < 95 and percent >= 94):
            return ("3.9")
        elif (percent < 94 and percent >= 93):
            return ("3.8")
        elif (percent < 93 and percent >= 92):
            return ("3.7")
        elif (percent < 92 and percent >= 91):
            return ("3.6")
        elif (percent < 91 and percent >= 90):
            return ("3.5")
        elif (percent < 90 and percent >= 89):
            return ("3.4")
        elif (percent < 89 and percent >= 88):
            return ("3.3")
        elif (percent < 88 and percent >= 87):
            return ("3.2")
        elif (percent < 87 and percent >= 86):
            return ("3.1")
        elif (percent < 86 and percent >= 85):
            return ("3.0")
        elif (percent < 85 and percent >= 84):
            return ("2.9")
        elif (percent < 84 and percent >= 83):
            return ("2.8")
        elif (percent < 83 and percent >= 82):
            return ("2.7")
        elif (percent < 82 and percent >= 81):
            return ("2.6")
        elif (percent < 81 and percent >= 80):
            return ("2.5")
        elif (percent < 80 and percent >= 79):
            return ("2.4")
        elif (percent < 79 and percent >= 78):
            return ("2.3")
        elif (percent < 78 and percent >= 77):
            return ("2.2")
        elif (percent < 77 and percent >= 76):
            return ("2.1")
        elif (percent < 76 and percent >= 75):
            return ("2.0")
        elif (percent < 75 and percent >= 74):
            return ("1.9")
        elif (percent < 74 and percent >= 73):
            return ("1.8")
        elif (percent < 73 and percent >= 72):
            return ("1.7")
        elif (percent < 72 and percent >= 71):
            return ("1.6")
        elif (percent < 71 and percent >= 70):
            return ("1.5")
        elif (percent < 70 and percent >= 69):
            return ("1.4")
        elif (percent < 69 and percent >= 68):
            return ("1.3")
        elif (percent < 68 and percent >= 67):
            return ("1.2")
        elif (percent < 67 and percent >= 66):
            return ("1.1")
        elif (percent < 66 and percent >= 65):
            return ("1.0")
        else:
            return ("0.0")
    elif (percent == -1):
        return ("Grading Finished")
    else:
        return ("Percent must be between 100 and 0")


gpa = float(input("Enter the grade:"))
print(compute_GPA(gpa))
while (gpa != -1):
    gpa = float(input("Enter the grade: "))
    print(compute_GPA(gpa))
