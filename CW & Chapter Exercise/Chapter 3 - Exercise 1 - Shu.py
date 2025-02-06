'''
Chapter 3 - Exercise 1
Name: Shu Z.
Get an input size from the user and compare it with 10.

'''

    i=1

    while(i<=3):
        size = int(input("Enter a number: "))
    if size < 10:
       print('Smaller')

    elif size > 10:
       print('Bigger')

    else:
        print('Fit')
    i+=1

print('Finish')

'''
Enter a number: 1
Smaller
Enter a number: 100
Bigger
Enter a number: 10
Fit
Finish
'''
