'''
Shu Zhu - Jan 13, 2025
This exercise calculates the gross pay 
using the hours and rate per hour which users input

Chapter 2 - Exercise 1
Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
'''
hours = float(input("Please eneter the hour: "))
rate = float(input("Please eneter the rate: "))
grossPay = hours*rate

print("The hour is", hours)
print("The rate is", rate)

print("The gross pay is", grossPay)

'''
Please eneter the hour: 
1
Please eneter the rate: 
20
The hour is 1.0
The rate is 20.0
The gross pay is 20.0

'''
