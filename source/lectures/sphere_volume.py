# A short program that computes the volume of a 
# sphere given a radius entered by the user.

# Have the user enter the radius and store it as a float
radius = float(input('Please enter a radius: '))

# Import the math module so that we have Pi
import math

# Compute the volume of the sphere
volume = (4/3)*math.pi*radius**3

# Print the volume
print("The volume is ", volume)