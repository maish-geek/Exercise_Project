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



#Question 1


fish = float(input("Enter the length of the Zander:"))
if fish < 42:
    print("A zander must be 42 cm. Please release the Zander!")



#Question 2




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





#Question 3

male = str(input("Enter gender:"))
hb = float(input("Enter haemoglobin value:"))

if (hb < 117):
    print("low Haemoglobin")
elif (hb >= 117 or hb <= 155):
    print("Normal Haemoglobin")
elif (hb > 155):
    print("High Haemoglobin")/n

if hb <134:
    print("Low Haemoglobin")
elif hb >=135 or hb <=167:
    print("Normal Haemoglobin")
elif hb >167:
    print("High Haemoglobin")



#Question 4

import sys

year = int(input("Enter year:"))
if(year%4 ==0 and year%100 !=0) or (year%400==0):
    print(year, "Is a leap year!")
else:
    print(year, "is not a leap year!")

sys.exit(0)
