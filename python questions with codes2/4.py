'''Determine the height of the tower that can be reached by the ladder, given the length and
angle in which the ladder has to be leaned on the tower. Write PAC, flowchart and python
code for determining the height of the tower. Length of the ladder is given in feet and angle to
lean the ladder is given in degrees. Display the height of the tower, with two decimal places.
Height of the tower = Length of the ladder * sine (Angle in radians).
Angle in radians = (Pi /180) * Angle in degrees'''
import math
n=int(input())
m=int(input())
angle=(3.14/180)*m
a=n*math.sin(angle)
b='{0:.2f}'.format(a)
print(b)