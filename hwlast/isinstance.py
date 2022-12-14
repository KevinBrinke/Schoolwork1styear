from CircleGeometricObject import Circle
from RectangleGeometricObject import Rectangle

def main():
    #Display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    print("Circle....")
    displayObject(c)
    print("Rectangle.....")
    displayObject(r)
    
#Display grometric object properties
def displayObject(g):
    print("Area is ", g.getArea())
    print("Perimeter is ", g.getPerimeter())

    if isinstance(g, Circle):
        print("Diameter is ", g.getDiameter())
    elif isinstance(g, Rectangle):
        print("Width is", g.getWidth())
        print("Height is", g.getHeight())

main()