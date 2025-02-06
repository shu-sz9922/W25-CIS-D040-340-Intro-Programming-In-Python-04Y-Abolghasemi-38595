'''
CIS 40 - Shu Z.
'''
'''
#use if loop to check the sqrt error, and use the function round() to fix it
import math

r=math.sqrt(2.0)

if r*r == 2.0:
    print ("sqrt(2.0) squared is 2.0")
else:
    print ("sqrt(2.0) squared is not 2.0 but", r*r)

#use round() to fix it
print ("sqrt(2.0) squared is", round(r*r))
'''

'''
#use elif to fix the problem of checing grades
grade = int(input("Enter student grade: "))
if grade >= 90 :
    letterGrade = "A"
elif grade >= 80 :
    letterGrade = "B"
elif grade >= 70 :
    letterGrade = "C"
elif grade >= 60 :
    letterGrade = "D"
else :
    letterGrade = "E"
print(letterGrade)
print("Finish")
'''

#combination of "if" and "and" to check conditions
temp= int(input("Enter: "))
if temp > 0 and temp < 100:
    print("Liquid")
print("temp > 0:",temp > 0)
print("temp < 100:",temp < 100)
print("temp > 0 and temp < 100:",temp > 0 and temp < 100)

#"or" and "not"
#and shortcut: False and () => False
#or shortcut: True and () => True


