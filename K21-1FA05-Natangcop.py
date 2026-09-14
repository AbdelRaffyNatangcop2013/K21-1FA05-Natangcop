"""
***Reflection:
The math library simplifies code by providing efficient, built-in functions like sqrt() and pow(). 
Using these built-in functions makes calculating Euclidean distance accurate and simple. 
Without them, manually writing algorithms for powers and square roots would give more complex things.
"""
import math

# Step 1: Collect coordinates for point 1 from user
point1_x = float(input("Enter x1: "))
point1_y = float(input("Enter y1: "))

# Step 2: Collect coordinates for point 2 from user
point2_x = float(input("Enter x2: "))
point2_y = float(input("Enter y2: "))

# Step 3: Calculate the distance between the points using the Euclidean distance formula.
distance = math.sqrt(math.pow(point2_x - point1_x, 2) + math.pow(point2_y - point1_y, 2))

# Step 4: Display the results
print(f"\nThe distance between the two points is: {distance:.2f}")
