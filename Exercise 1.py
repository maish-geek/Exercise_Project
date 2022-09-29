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

#Question 5.2
print("Input integers with a pace between:")
nums = list(map(int, input().split()))
dsc_nums = sorted(nums, reverse=True)
print("Descending Numbers: ", dsc_nums)



main()

#Question 5.3

num = int(input("Enter a number: "))

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")


else:
    print(num, "is not a prime number")

#Question 5.4

print("Input five cities:")
cities = list(map(str, input().split()))
for city in cities:
    print(city)
  
#Question 6.1

def dice_roll():
    return random.randint(1,6)

value = dice_roll()

while value != 6:
    print("The result of dice rolled is", value)
    value = dice_roll()
    if value == 6:
        print("End of rolling because you have a", value)
      
#Question 6.2

import random

def main():
  
    while True:
        num_dice = int(input('How many dice do you want to roll?'))
        if num_dice < 1 or num_dice > 6:
            print('Enter a number between 1 and 6.')
        else:
            break
    result = roll_dice(num_dice)
    print(f'The total for {num_dice} rolls was {result}.')


def roll_dice(num_dice):
    rolls = 0
    for i in range(1, num_dice + 1):
       
        print(f'Roll #{i} = {(roll := random.randint(1, 21))}')
        rolls += roll
    return rolls


main()

#Question 6.3

def conver_gal(lit):
    conversion = 3.7854 * lit
    return conversion

fuel = int(input("Enter the volume of your gasoline in US.gallons:"))
print(f"{conver_gal(fuel):.2f} litres")

#Question 6.4

def list_int(values):
    sum = sum(values)
    print(sum)

list1 = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]

(list_int(list1))

#Question 6.5

def con_value(slave):
    for num in slave:
        if num % 2 == 0:
            list_2.append(num)
    print("Here is the original list", slave)
    print("Here is the list without uneven numbers", list_2)

list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_2 = []

con_value(list_1)

#Question 6.6

def pizza_price(pizza_diameter, unit_price):

    area_pizza = 3.143 * (pizza_diameter/2)**2
    single = unit_price/ area_pizza
    return single

size_rosapizza = int(input("Enter the diameter size of Rosa pizza:"))
size_hutpizza = int(input("Enter the diameter size of Hut pizza"))
price_rosapizza = float(input("Enter the price of the Rosa pizza option"))
price_hutpizza = float(input("Enter the price of the Hut pizza option"))

rosapizza = pizza_price(size_rosapizza, price_rosapizza)
hutpizza = pizza_price(size_hutpizza, price_hutpizza)

print(f"{rosapizza:2f} euro per m2")
print(f"{hutpizza:2f} euro per m2")

if rosapizza < hutpizza:
    print("Rosa Pizza has a much lower unit price")

else:
    print("Hut Pizza has a much lower unit price")

  

#Question 7.1

my_tuple = ('spring', 'summer', 'autumn', 'winter')
month = input("Input the month number: ")
if month=='12' or month=='1' or month=='2':
    print(my_tuple[3])
if month=='3'or month=='4'or month=='5':
    print(my_tuple[0])
if month=='6' or month=='7' or month=='8':
    print(my_tuple[1])
if month=='9' or month=='10' or month=='11':
    print(my_tuple[2])


#Question 7.2

while True:
    user_input = input("Please enter a name :")
    myset.add(user_input)
    if user_input == '':
        break

    print(myset)

#Question 7.3

import sys

airports = {"ATL": "Hartsfield–Jackson Atlanta International Airport",
            "AMS": "Amsterdam Airport Schiphol",
            "DEL": "Indira Gandhi International Airport (Delhi)",
            "CAN": "Guangzhou Baiyun International Airport",
            "FRA": "Frankfurt Airport",
            "DFW": "Dallas/Fort Worth International Airport",
            "ICN": "Seoul Incheon International Airport",
            "IST": "Istanbul Atatürk Airport",
            "CGK": "Soekarno-Hatta International Airport",
            "SIN": "Singapore Changi Airport",
            "DEN": "Denver International Airport",
            }

while True:
    user_input = input(
        "Do you want to  enter a new airport(enter), fetch the information of an existing airport(fetch) or quit(q)")
    if user_input == 'q':
        break
    if user_input == 'enter':
        enter = input("Enter a ICAO number and name of Airport:")
        print(enter)
    if user_input == 'fetch':
        code = input("Enter a 3-letter airport code:").upper()
        while len(code) != 3:
            print("Invalid airport code.")
            code = input("Enter a 3-letter airport code:").upper()
        while not code in airports:
            print("Airport code not recognised. Please try again with a different airport code.")
            code = input("Enter a 3-letter airport code:").upper()
        print(airports[code])

#Question 8.1

import mysql.connector

conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="NjugunaM@93",
                               database="flight_game"
                               )

user = input("Enter the ICAO code of any airport:")
config = conn.cursor()
config.execute("select name, location from airports, game where ident = " + "'" + user + "'")

for i in config:
    print(i)

#Question 8.2

import mysql.connector

conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="NjugunaM@93",
                               database="flight_game"
                               )

user = input("Enter the area code of any country:")
synt = "select name, type from airports, where iso_country = " + "'" + user + "'" + "order by type desc"
config = conn.cursor()
config.execute(synt)

for i in config:
    print(i)


  
#Question 8.3

import mysql.connector
import geopy
from geopy import distance

conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="NjugunaM@93",
                               database="flight_game"
                               )

icao_code1 = input("Enter the first ICAO code")
icao_code2 = input("Enter the second ICAO code")

sql = "select latitude_deg, longitude_deg from airport where ident = " + "'" + icao_code1 + "'"
stm = "select latitude_deg, longitude_deg from airport where ident = " + "'" + icao_code2 + "'"

con_fig = conn.cursor()
con_fig.execute(sql)

for i in con_fig:
    print(i)

con_fig.execute(stm)
for j in con_fig:
    print(j)

print(distance.distance(i, j).km)
  
  
