'''
Name: Shu Z.

Chapter 3 - Exercise 2
Have wrote a program to prompt the user for hours and rate per hour to compute gross pay.
Rewrite the pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

s
475 = 40 * 10 + 5 * 15

Run your code with two different numbers and put the results at the end of your code as a multi-line comment.
'''

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
if hours > 40:
    pay = 40*rate + (hours-40)*1.5*rate
else:
    pay = hours*rate
print("Pay:", pay)

'''
Enter Hours: 50
Enter Rate: 10
Pay: 550.0

Enter Hours: 40
Enter Rate: 10
Pay: 400
'''
