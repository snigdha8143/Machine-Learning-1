#the radius of circle given is 30
from math import pi                                       # importi pi from math module
r = 30                                                    # the radius given = 30
area_of_circle = pi*r*r                                  # Find the area of circle
print("Area of circle the with radius 30 is " + str(area_of_circle))   # to print the area of circle

circum_of_circle = 2*pi*r                                              # to find the circumference of the circle
print("Circumference of circle the with radius 30 is " + str(circum_of_circle))     # to print the circumference of the circle

radius = float(input("Enter the radius of circle"))       # considering the radius as input from the user
area_of_circle_new_radius = pi*radius*radius                  # Find the area of circle using the radius from user input
print("Area of circle the with radius "+str(radius) + " is " + str(area_of_circle_new_radius)) # Print  area of circle

