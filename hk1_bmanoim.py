"""Bella Manoim's HW 01: Testing Triangle Classification

Recall that:
- equilateral triangles have all three sides with the same length
- isosceles triangles have two sides with the same length
- scalene triangles have three sides with different lengths
- right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
Your assignment is to write a program in Python to classify triangles and use an automated test platform,
e.g. UnitTest or PyTest, and write test cases to test your implementation of classifying triangles.
The goal is for you to gain experience using automated test tools and to think through the issues
associated with testing a "system".

“Write a function classify_triangle() that takes three  parameters: a, b, and c. The three parameters
represent the lengths of the sides of a triangle. The function returns a string that specifies whether
the triangle is scalene, isosceles, or equilateral, and whether it is a right triangle as well.”

Hint:  Write a function called classify_triangle(a, b, c) where a, b, and c are the lengths of the sides
of the triangles.   You may either allow the user to enter values that you pass to classify_triangle() or
your "main" routine can just invoke classify_triangle() with values.   This approach allows you to easily
invoke classify_triangle() from your test framework.


"""
import UnitTest

greeting = 'Hello, this program will determine classify triangles based on the 3 side values.'

print(greeting)

triangeType = ''

def classify_triangle(a,b,c):
    if a == b == c:
        triangleType = 'This is an equilateral triangle'
    elif (a == b and b != c) or (a == c and b != c) or (b == c and b != a):
        triangleType = 'This is an isosceles triangle'
    elif (a != b and a != c and b != c):
        triangleType = 'This is a scalene triangle'
    if ((a * a) + (b * b) == (c * c)):
        triangleType = triangleType + ' and right triangle'
    print(triangleType)

try:
    classify_triangle(2,2,3)
    classify_triangle(3,4,5)
    classify_triangle(1,2,3)
    classify_triangle(2,2,2)
    classify_triangle(5,12,13)
    classify_triangle(5,5,5)
    classify_triangle(5,2,5)
except:
    print ('Only integer values allowed. Please run program again.\n')
