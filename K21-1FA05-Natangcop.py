"""
***Reflection:
The math library simplifies code by providing efficient, built-in functions like sqrt() and pow(). 
Using these built-in functions makes calculating Euclidean distance accurate and simple. 
Without them, manually writing algorithms for powers and square roots would give more complex things.
"""
import math

# Step 1: Collect coordinate inputs from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Step 2: Calculate the distance between the points using the Euclidean distance formula.
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Step 3: Display the results
print(f"\nThe distance between the two points is: {distance:.2f}")
