import math

AB = int(input())
BC = int(input())

# In a right triangle, tan(angle) = opposite/adjacent
# angle MBC = arctan(AB/BC)
angle_radians = math.atan(AB / BC)

# Convert to degrees and round to nearest integer
angle_degrees = round(math.degrees(angle_radians))

degree = chr(176)  # Unicode character for degree symbol

print(str(angle_degrees) + degree)