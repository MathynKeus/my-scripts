"""
Learn Python - Full Course for Beginners [Tutorial]
#https://www.youtube.com/watch?v=rfscVS0vtbw&t=7054s
"""

#variables_strings
character_name = "Mathyn"
print("The name is: " + character_name)
character_age = "18" 
print("The age is :" + character_age)

#variables_strings_integers
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

#example_of_functions
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

#Integers_numbers
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

#imports_a_bunch_of_math_functions
from math import *
print(floor(3.7)) #grabs the lowest number

#input_from_users
name = input("Enter your name:")
print("Hello " + name)

#input_name_and_age
name = input("Enter your name:")
age = input("Enter your age")
print("Hello " + name + "You are " + age + " years old")

#calculator
num1 = input("Enter a number")
num2 = input("Enter a second number")
result = int(num1) + int(num2)
print(result)

#calculator_with_decimal_numbers
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

#lists_functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Swiper", "Boots", "Dora", "Diego", "Jeff"]
friends.append("Kees")
friends.extend(lucky_numbers)
friends.insert(1, "Jan")
friends.remove("Swiper")
friends.clear()
friends.sort()
print(friends.index("Jeff"))
print(friends.__contains__("Jeff"))

friends2 = friends.copy()
print(friends2)

#tuples
coordinates = (4, 5), (6,7), (8,9)
print(coordinates[0])

#functions
def say_hi(name, age):
    print("Hello " + name + " You are " + str(age))

say_hi("Mike", 33)

#return_statement
def cube(num):
    return num*num*num

result = cube(3)
print(result)

#if_statements
is_male = True
is_tall = True

if is_male:
    print("You are a male")
else: 
    print("You are a female")

#or statement
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male")
else: 
    print("You are a female")

#and statement
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male")
else: 
    print("You are a female")

#else_if + not_statement
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not is_male and is_tall:
    print("You are a short male")
else: 
    print("You are a female")

#functions_and_parameters
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,15,40))

#building_a_better_calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

#dictionaries
monthConversions = {
    "Jan": "January",
    1: "February",
    "Mar": "March",
}

print(monthConversions["Jan"])
print(monthConversions.get(1))
print(monthConversions.get("Jeff", "Not a valid key"))

#while_loop
i = 1
while i <= 10:
    print(i) 
    i = i + 1

print("Done with loop")

#guessing_game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose the game")
else:
    print("You win the game")

#for_loop
for letter in "Jeff":
    print(letter)

friends = ["Jeff", "Diego", "Swiper"]
for friend in friends:
    print(friend)

friends = ["Jeff", "Diego", "Swiper"]
for index in range(10):
    print(index)

friends = ["Jeff", "Diego", "Swiper"]
for index in range(3, 10):
    print(index)

#exponent_function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))

#2D_lists 
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[1][1])

#nested_loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

#building_a_translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
            
    return translation

print(translate(input("Enter a phrase: ")))