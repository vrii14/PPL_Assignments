'''In this implementation of classes Shape is the parent class and inherits all the other classes. It contains the abstract methods which are defined in the
    child classes. The flow is as follows:
    1. Shape is the base class
    2. Line, Polygon and Ellipse are the derived classes of Shape
    3. Circle is derived class of Ellipse
    4. Triangle and Rectangle are derived classes of Polygon
    5. Square is derived class of Rectangle
    6. Equilateral Triangle is derived class of Triangle
    At the end all the methods are called by creating objects of respecting classes.

    Also the draw methods will run one after another. So each can be demonstrated by commenting others.
'''


from abc import ABC,abstractmethod
from math import sqrt
import turtle
import math

class Shape(ABC):
    
    #common function
    def shape(self):
        print("I am a shape")
        
    @abstractmethod
    def side(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def draw(self):
        print("I will draw a shape")



class Line(Shape):
    
    def __init__(self, length = 10):
        self.length = length
        
    
    def side(self):
        print("I am a line and my length is {}".format(self.length))
        
    def perimeter(self):
        print("Perimeter of line is its length i.e. {}".format(self.length))
        
    def area(self):
        print("My area is zero.")
        
    def draw(self):
        print("I will draw a line")
        line = turtle.Turtle()
        line.forward(self.length)
        
        turtle.resetscreen()


class Polygon(Shape):
    
    def draw(self):
        print("I will draw a polygon")




class Triangle(Polygon):
    
    def __init__(self, side1 = 10, side2 = 10, side3 = 15):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def side(self):
        print("I have three sides")
        
    def perimeter(self):
        print("Perimeter of the triangle is: {}".format(self.side1 + self.side2 + self.side3))
        
    def area(self):
        sp = (self.side1 + self.side2 + self.side3)/3
        print("Area of the triangle is: {}".format(abs(sqrt(sp*(sp-self.side1)*(sp-self.side2)*(sp-self.side3)))))
        
    def draw(self):
        print("I will draw a triangle")


class Rectangle(Polygon):
    def __init__(self, lengthh = 15, breadth = 10):
        self.lengthh = lengthh
        self.breadth = breadth
        
    def side(self):
        print("I have four sides.")
        
    def perimeter(self):
        print("Perimeter of the rectangle is: {}".format(2*(self.lengthh + self.breadth)))
    
    def area(self):
        print("Area of rectangle is: {}".format(self.lengthh*self.breadth))
        
    def draw(self):
        print("I will draw a rectangle.")
        rect = turtle.Turtle()

        for i in range(2): 
            rect.forward(self.lengthh)
            rect.right(90)     # Rotate clockwise by 90 degrees
            rect.forward(self.breadth)
            rect.right(90)
        
        turtle.resetscreen()



class Equilateraltriangle(Triangle):
    
    def __init__(self, sidee = 10):
        self.sidee = sidee
        
    def side(self):
        print("I have three equal sides.")
        
    def perimeter(self):
        print("Perimeter of the equilateral triangle is: {}".format(3*self.sidee))
        
    def area(self):
        print("Area of equilateral triangle is: {}".format(sqrt(3)*self.sidee*self.sidee/4))
        
    def draw(self):
        print("I will draw an equilateral triangle.")
        board = turtle.Turtle()
 
        board.forward(self.sidee) # draw base
         
        board.left(120)
        board.forward(self.sidee)
         
        board.left(120)
        board.forward(self.sidee)

        turtle.resetscreen()


class Ellipse(Shape):
    
    pi = 3.14
    
    def __init__(self, a = 10, b = 8):
        self.a = a
        self.b = b
        
    def side(self):
        print("I have infinite sides")
    
    def perimeter(self):
        pass
    
    def area(self):
        print("Area of ellipse is: {}".format(self.pi*self.a*self.b))
        
    def draw(self):
        print("I will draw an ellipse.")
        for i in range(361):
            t = i * (self.pi / 180)
            x = (self.a) * math.sin(t)
            y = (self.b) * math.cos(t) - self.b
              #turtle.goto(x,y)
            tilt = 25 * (math.pi / 180)
            x1 = x * math.cos(tilt) + y * math.sin(tilt)
            y1 = x*math.sin(tilt) - y*math.cos(tilt)
            turtle.goto(x1,y1)

        turtle.resetscreen()


class Circle(Ellipse):
    
    def __init__(self, radius = 10):
        self.radius = radius
        
    def side(self):
         print("I have infinite sides")
    
    def perimeter(self):
        print("Perimeter of circle is: {}".format(2*self.pi*self.radius))
        
    def area(self):
        print("Area of circle is: {}".format(self.pi*self.radius*self.radius))
        
    def draw(self):
        print("I will draw a circle")
        cir = turtle.Turtle()
        cir.circle(self.radius)
        
        turtle.resetscreen()


class Square(Rectangle):
    
    def __init__(self, s = 10):
        self.s = s
        
    def side(self):
        print("I have 4 sides.")
        
    def perimeter(self):
        print("The perimeter of square is: {}".format(4*self.s))
        
    def area(self):
        print("Area of square is: {}".format(self.s* self.s))
        
    def draw(self):
        print("I will draw a square.")
        square = turtle.Turtle()
        
        for i in range(4):
            square.forward(self.s)
            square.right(90)

        turtle.resetscreen()



my_line = Line(20)
my_line.side()
my_line.perimeter()
my_line.area()
my_line.draw()

my_triangle = Triangle(10, 20, 30)
my_triangle.side()
my_triangle.perimeter()
my_triangle.area()
my_triangle.draw()

my_rectangle = Rectangle()
my_rectangle.side()
my_rectangle.perimeter()
my_rectangle.area()
my_rectangle.draw()

my_ellipse = Ellipse(10, 20)
my_ellipse.side()
my_ellipse.perimeter()
my_ellipse.area()
my_ellipse.draw()

my_eqtr = Equilateraltriangle(12)
my_eqtr.side()
my_eqtr.perimeter()
my_eqtr.area()
my_eqtr.draw()

my_square = Square(15)
my_square.side()
my_square.perimeter()
my_square.area()
my_square.draw()

my_circle = Circle(10)
my_circle.side()
my_circle.perimeter()
my_circle.area()
my_circle.draw()
