#By Fabian Hasin
#Please run it on "Visual Studio Code" for guaranteed best experience.
#Currently only works with the following shapes: rectangle, square, triangle, circle, trapezoid, rhombus, parallelogram

from subprocess import call

while True:
    Shape = input("Shape: ")
    if Shape.lower() == "rectangle":
        call(["python", "Rectangle.py"])
    elif Shape.lower() == "square":
        call(["python", "Square.py"])
    elif Shape.lower() == "triangle":
        call(["python", "Triangle.py"])
    elif Shape.lower() == "circle":
        call(["python", "Circle.py"])
    elif Shape.lower() == "trapezoid":
        call(["python", "Trapezoid.py"])
    elif Shape.lower() == "rhombus":
        call(["python", "Rhombus.py"])
    elif Shape.lower() == "parallelogram":
        call(["python", "Parallelogram.py"])
    elif Shape.lower() != ["rectangle", "square", "triangle", "circle", "trapezoid", "rhombus", "parallelogram"]:
        print("Enter a valid shape.")
