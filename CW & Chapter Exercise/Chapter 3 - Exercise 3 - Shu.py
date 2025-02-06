'''
CIS 340 
Chapter 3 - Exercise 3 - Shu Zhu

Rewrite the pay program using try and except 
so that the program handles non-numeric input gracefully. 
Also, use the "isdigit" method (assume the user enters non-float numbers) 

FE:
Enter Hours: 20

Enter Rate: nine

Error, please enter numeric input

Enter Hours: forty 

Error, please enter numeric input

 

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
if hours > 40:
    pay = 40*rate + (hours-40)*1.5*rate
else:
    pay = hours*rate
print("Pay:", pay)

'''


# def turnInt(intp):
#     if(intp.isdigit()):
#         intp = int(intp)
#     else:
#         return -1
        

try:
    hours = int(input("Enter Hours: "))
except:
    print("Error, please enter numeric input")
    hours = int(input("Enter Hours: "))


try:
    rate = int(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    rate = int(input("Enter Rate: "))

if (hours > 40):
    pay = 40*rate + (hours-40)*1.5*rate
else:
    pay = hours*rate
   
print("Pay:", pay)


'''
= RESTART: E:/OneDrive - Foothill DeAnza CCD/##25Win/CIS 340/Chapter 3 - Exercise 3 - Shu Zhu.py
Enter Hours: 20
Enter Rate: 20
Pay: 400

= RESTART: E:/OneDrive - Foothill DeAnza CCD/##25Win/CIS 340/Chapter 3 - Exercise 3 - Shu Zhu.py
Enter Hours: 200
Enter Rate: 20
Pay: 5600.0

= RESTART: E:/OneDrive - Foothill DeAnza CCD/##25Win/CIS 340/Chapter 3 - Exercise 3 - Shu Zhu.py
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Rate: 9
Pay: 180

= RESTART: E:/OneDrive - Foothill DeAnza CCD/##25Win/CIS 340/Chapter 3 - Exercise 3 - Shu Zhu.py
Enter Hours: nine
Error, please enter numeric input
Enter Hours: 9
Enter Rate: forty
Error, please enter numeric input
Enter Rate: 40
Pay: 360
'''
