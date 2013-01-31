# Name: Jessie Daubner
# Date: January 24, 2013

################################################################
# function name: is_triangle1
# param: three -- a, b, c the side of a triangle
# desc:  take 3 integers as arguments and if a + b > c, print 
# "No" and if a + b < c, print "Yes"  
# returns: None
################################################################
def is_triangle(a, b, c):
	sum = a + b
	if sum > c:
		print("No")
	else:
		print("Yes")

ex1 = is_triangle(5, 7, 13)
print ex1

################################################################
# func name: get_ints
# param: three -- d, e, f 
# desc: get three integers from the user
# returns: three integers
################################################################
def get_ints():
	d, e, f = input ("Please enter three integers, each separated by a comma: ")
	return d, e, f 
a, b, c = get_ints()
is_triangle(a, b, c)
