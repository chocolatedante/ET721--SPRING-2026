"""
Dante Vanderpool 
Feb 5 2026
Lab 5, function
"""
import math 
#example 1
def area_rectangle(width, length):
    return width*length

#void fucntion doesnt return a value
def print_area_result(width, length, area):
    print(f'The area of rectanlge of {width} and {length} is {area}')

#example 2: calculate the distance of two points
#distance = square_root of ((x2-x1)^2 + (y2-y1)^2)
#function 1) collect a number between 1 and 10
def collectnum():
    num=int(input("Enter a number: "))
    #use a loop to recollect the number if the number is not between 1 and 10 
    while(num<1 or num>10):
        num=int(input("Invlalid. Enter a number between 1 and 10: "))
    return num

#function that calcluates and returns the distance
#distance = square_root of ((x2-x1)^2 + (y2-y1)^2)
def calculate_distance(x1,x2,y1,y2):
    return math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

#function to print the result
def print_distance(x1,x2,y1,y2, distance):
    print(f"The distance of points ({x1},{y1}) and ({x2},{y2} is {round(distance,2)})")

    #EXERCISE

import random

def collect_random(min_num, max_num):
    return random.randint(min_num, max_num)

def print_guess_result(random_num, guess_num):
    if random_num < guess_num:
        print("The number is smaller than the guess number")
    elif random_num > guess_num:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")
