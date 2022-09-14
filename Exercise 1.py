#QUESTION 1.1

#print("Hello, Wallace Njuguna!")

#QUESTION 1.2
# created Github account and linked with pycharm

#Variables and Interactive Programs

#QUESTION 2.1

#user = input("Enter your Name:")

#print("Hello," + user + "!")

#QUESTION 2.2

#from math import pi

#r = float(input ("input the radius of the circle : "))

#print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# QUESTION 2.3

#l=int(input("Length : "))

#w=int(input("Width : "))

#area=l*w

#perimeter=2*(l+w)

#print("Area of Rectangle : ",area)

#print("Perimeter of Rectangle : ",perimeter)

#QUESTION 2.4

#x = int(input("Please enter the first Value: "))
#y = int(input("Please enter the second value: "))

#print("sum = {}".format(x+y))
#print("product = {}".format(x*y))
#print("average = {}".format((x+y)/2))

#QUESTION 2.5

#QUESTION 2.6

#from random import randint
#threedigitcode = ""
#for x in range (3):
 #   threedigitcode = threedigitcode + str(randint(0,9))
#print(threedigitcode)

#fourdigitcode = ""
#for y in range(4):
 #   fourdigitcode = fourdigitcode + str(randint(1,6))
#print(fourdigitcode)



#Question 3.1

fish = float(input("Enter the length of the Zander:"))
if fish < 42:
    print("A zander must be 42 cm. Please release the Zander!")



#Question 3.2

cabin = str(input("Enter a cabin class: "))

if cabin == str("lux"):
    print("Upper-deck cabin with a Balcony!")
elif cabin == str("A"):
    print ("Above the car deck, equipped with a window.")
elif cabin == str("B"):
    print("Windowless cabin above the car deck.")
elif cabin == str("C"):
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class!!")


#Question 3.3

gender = input("Enter your biological gender Male or Female: ")
g_l = float(input("Enter haemoglobin value:"))

if gender == "Female":

    if (g_l < 117):
        print("low Haemoglobin")
    elif (g_l >= 117 and g_l <= 155):
        print("Normal Haemoglobin")
    else:
        print("High Haemoglobin")

if gender == "Male":

    if g_l <134:
        print("Low Haemoglobin")
    elif g_l >=135 and g_l <=167:
        print("Normal Haemoglobin")
    else:
        print("High Haemoglobin")



#Question 3.4

import sys

year = int(input("Enter year:"))
if(year%4 ==0 and year%100 !=0) or (year%400==0):
    print(year, "Is a leap year!")
else:
    print(year, "is not a leap year!")

sys.exit(0)






# Python program to print numbers divisible by 3 using while loop

#Question 4.1

start = int(input("Enter start number:"))
end = int(input("Enter last number:"))
while(start<=end):
    if(start%3==0):
      print(start)
    else:
        print("Not Divisible!")
start += 1

#Question 4.2

inches = float(input('Enter the Height in inches to convert into centimeters:'))

centi_meters = inches * 2.54
centi_meters = round(centi_meters,2)

print(inches,'Inches =', centi_meters,'Centimeters')


#Question 4.3

current_number = int(input("Enter numbers:"))
lowest = current_number
highest = current_number

while current_number != "":
    if current_number <lowest:
        lowest = current_number
    if current_number >highest:
        highest = current_number

current_number = input("Enter numbers:")
if current_number != "":
    current_number = int(current_number)

    print("lowest:", lowest, "highest:", highest)


#Question 4.4



#Question 4.5

print('Enter correct username and password combo to continue')
count=0
password=rules
username=python

while password!='rules' and username!='python' and count<5:
    username=input('Enter username: ') and password=input('Enter password: ')

    if password=='rules' and username=='python':
     print('Welcome')

    else:
        print('Access denied. Try again.')
        count-=1

       
       import sys

#Question 5.1

import random


def main():
    while True:

        num_dice = int(input('How many dice do you want to roll?'))
        if num_dice < 1 or num_dice > 10:
            print('Enter a number between 1 and 10.')
        else:
            break
    result = roll_dice(num_dice)
    print(f'The total for {num_dice} rolls was {result}.')


def roll_dice(num_dice):
    rolls = 0
    for i in range(1, num_dice + 1):
        print(f'Roll #{i} = {(roll := random.randint(1, 6))}')
        rolls += roll
    return rolls


main()

#Question 5.3

x = input('Enter an integer: ')
prime = True  # initial set

for i in range(2, x):
    if x % i == 0:
        prime = False
        break

if prime:
    print(str(x) + ' is prime.')
else:
    print(str(x) + ' is not prime')
