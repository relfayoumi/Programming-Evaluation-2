#Import sys to be able to use the sys.exit() function
import sys

#Ask the user for 4 grades and variables
course1 = float(input("Enter the first grade: "))
course2 = float(input("Enter the second grade: "))
course3 = float(input("Enter the third grade: "))
course4 = float(input("Enter the fourth grade: "))
letterGrade = ""
#Check if one of the grades is higher than 100 or less than 0
if course1 > 100 or course1 < 0 or course2 > 100 or course2 < 0 or course3 > 100 or \
        course3 < 0 or course4 > 100 or course4 < 0:
  print("Rerun the program, grades cannot exeed 100 or fall below 0")
  sys.exit()

#Calculate the average
average = (course1 + course2 + course3 + course4) / 4

#Calculate the letter grade
if average >= 95 and average <= 100:
  letterGrade = "A+"
elif average <= 94 and average >= 87:
  letterGrade = "A"
elif average <= 86 and average >= 80:
  letterGrade = "A-"
elif average <= 79 and average >= 77:
  letterGrade = "B+"
elif average <= 76 and average >= 72:
  letterGrade = "B"
elif average <= 71 and average >= 70:
  letterGrade = "B-"
elif average <= 69 and average >= 67:
  letterGrade = "C+"
elif average <= 66 and average >= 63:
  letterGrade = "C"
elif average <= 62 and average >= 60:
  letterGrade = "C-"
elif average <= 61 and average >= 57:
  letterGrade = "D+"
elif average <= 56 and average >= 54:
  letterGrade = "D"
elif average <= 53 and average >= 50:
  letterGrade = "D-"
elif average <= 49 and average >= 0:
  letterGrade = "F"

#Print average and letter grade
print("\nYour average grade is", round(average, 2), "which means your letter grade is",
      letterGrade)
