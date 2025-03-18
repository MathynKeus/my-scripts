"""
Learn Python - Full Course for Beginners [Tutorial]
#https://www.youtube.com/watch?v=rfscVS0vtbw&t=7054s
"""

#variables (string)
character_name = "Mathyn"
print("The name is: " + character_name)
character_age = "18" 
print("The age is :" + character_age)

#variables (string + integer)
character_name = "Mathyn"
print("The name is: " + character_name)
character_age = 18 
print("The age is :" + str(character_age))

#boolean
is_male = True
is_female = False

#newline 
print("Hello,\nWorld!")

#printliterally 
print("hello\"World")

#printvariable
name = "Mathyn"
print(name)

#functions
name = "Mathyn"
print(name.lower()) #name in lower case
print(name.isupper()) #check if name is uppercase, true or false.
print(name.upper().isupper()) #functions in combination with each other
print(len(name)) #function to show how many characters in variable 
print(name[0]) #show letter in position 0 of variable 
print(name.index("n")) #return the index (position) of "n" in variable
print(name.index("Mathyn"))
print(name.index("athyn"))
print(name.replace("Mathyn", "mathyn"))

#Integers (numbers)
print(3 * 4 + 5)
print (3 * (4 + 5)) #basic math lol
print (10 % 3) #show remainder

my_num = 8
print(my_num)
print(str(my_num)) #convert int > str
print(str(my_num) + " is my favorite number") #print int as str with str
print(max(4,6)) #prints the higher number
print(min(4,6)) #prints the lower number
print(round(3.2)) #rounds the number

#imports a bunch of math functions
from math import *
print(floor(3.7)) #grabs the lowest number

#input from users
name = input("Enter your name:")
print("Hello " + name)

#input name + age
name = input("Enter your name:")
age = input("Enter your age")
print("Hello " + name + "You are " + age + " years old")

#calculator
num1 = input("Enter a number")
num2 = input("Enter a second number")
result = int(num1) + int(num2)
print(result)

#calculator with decimal numbers
num1 = input("Enter a number")
num2 = input("Enter a second number")
result = float(num1) + float(num2)
print(result)

#madlibsgame
color = input("Enter a color")
plural_noun = input("Enter a plural noun")
celebrity = input("Enter a celebrity")

print("Roses are " + color ) 
print(plural_noun + " are blue")
print("I love " + celebrity)

#lists
friends = ["Swiper", "Boots", "Dora", "Diego", "Jeff"]
print(friends[0])
print(friends[0:4]) #position 0 -> 4
print(friends[0], friends[4]) #position 0 + 4