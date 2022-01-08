'''
consol Program to calculate angle and length in a triangle

	     C    
	    /\\    
	 a /  \\ b
	  /____\\ 
	 B  c    A
'''
import math as math


class triangle:
	a = 0.0
	b = 0.0
	c = 0.0
	A = 0.0
	B = 0.0
	C = 0.0
	area = 0.0
	height = 0.0
	length2C = 0.0
	#isOptuse = False

#funktion to draw triangle with value
def drawTriangle(tri = triangle()):
	#\\ = print \
	print("     C    ")
	print("    /\\   ") 
	print(" a /  \\ b")
	print("  /____\\ ")
	print(" B  c    A")
	print("A = " + str(tri.A))
	print("B = " + str(tri.B))
	print("C = " + str(tri.C))
	print("\n")
	print("a = " + str(tri.a))
	print("b = " + str(tri.b))
	print("c = " + str(tri.c))
	print()
	print("length2C = " + str(tri.length2C))
	print("height = " + str(tri.height))
	print("area = " + str(tri.area))


#Draw a triangle without value
def drawTriangleSimp():
	#\\ = print \
	print("     C    ")
	print("    /\\   ") 
	print(" a /  \\ b")
	print("  /____\\ ")
	print(" B  c    A")

def inputFloat(komment):
	while True:
		try:
			x = input(komment)
			return float(x if x != "" else "0")
		except ValueError:
			print("Need a number")

def inputTriangle():
	drawTriangleSimp()
	print("\n")
	tri = triangle()
	print("Uppercase = angle, Lowercase = length")
	print("0 if unknown\n")
	#tri.A = inputFloat("A = ")
	#tri.B = inputFloat("B = ")
	#tri.C = inputFloat("C = ")
	print()
	tri.a = inputFloat("a = ")
	tri.b = inputFloat("b = ")
	tri.c = inputFloat("c = ")
	return tri

#rotate c to the lowest position
def rotateTriangle(tri):
	#make c the highest number
	while(tri.c < tri.a and tri.c < tri.b):
		tempa = tri.a
		tempb = tri.b
		tempc = tri.c
		
		tri.a = tempc
		tri.b = tempa
		tri.c = tempb

	return tri

#the math is shown in a separate onenote document
def calculateTriangle(tri):
	if(tri.a != 0 and tri.b != 0 and tri.c != 0):
		#if tri.length2C = 0, it's 90 degrees and we rotate it to make the formula work.
		# rotate everytime because it never hurt and we ignore negative formula (potential from obtuse triangle)
		# and potential problem with non return 0 from right-angle triangels 
		tri = rotateTriangle(tri)
		#formula for the length on the x'axis to the highest point on y'axis (proven in math document)
		tri.length2C = (tri.c**2+tri.a**2-tri.b**2)/(2*tri.c) 
		#tri.length2C = (pow(tri.b, 2)+pow(tri.a,2) - pow(tri.c,2))/(2*tri.b) 
		
		
		#Pythagoras theorem for height
		tri.height = math.sqrt(tri.a**2 - tri.length2C**2)
		#angle of tri.X
		try:
			tri.B = math.degrees(math.atan(tri.height/tri.length2C))
		except ZeroDivisionError:
			print("division with zero angel A, fix comming soon")
		try:
			tri.A = math.degrees(math.atan(tri.height/(tri.c-tri.length2C) ) )
		except ZeroDivisionError:
			print("division with zero angel A, fix comming soon")
		#for C, add together "left triangle" and "right triangle"
		try:
			lC = math.degrees(math.atan(tri.length2C/tri.height))
			rC = math.degrees(math.atan((tri.c-tri.length2C)/tri.height))
			tri.C = lC+rC
			
		except ZeroDivisionError:
			print("division with zero angel lC, fix comming soon")
			print("division with zero angel rC, fix comming soon")
	
		#formula för area
		tri.area = tri.length2C * tri.height / 2
		return tri
		
tri = inputTriangle()
tri = calculateTriangle(tri)
drawTriangle(tri)
input()