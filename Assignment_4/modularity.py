from animals import *
from shapes import *
from math import sqrt
import turtle
import math

if __name__ == '__main__':
	
	#animals
	my_deer = Deer("Bucky", 29)
	my_deer.name()
	my_deer.age()
	my_deer.eat()
	my_deer.speak()

	my_cow = Cow("Emma", 36)
	my_cow.name()
	my_cow.age()
	my_cow.eat()
	my_cow.speak()


	my_cat = Cat("Misty", 20)
	my_cat.name()
	my_cat.age()
	my_cat.eat()
	my_cat.speak()

	my_lion = Lion("Simba", 38)
	my_lion.name()
	my_lion.age()
	my_lion.eat()
	my_lion.speak()


	my_bear = Bear("Fuzzy", 45)
	my_bear.name()
	my_bear.age()
	my_bear.eat()
	my_bear.speak()

	my_human = Human("Shyam", 30)
	my_human.name()
	my_human.age()
	my_human.eat()
	my_human.speak()

	my_line = Line(50)
	my_line.side()
	my_line.perimeter()
	my_line.area()
	my_line.draw()

	my_triangle = Triangle(10, 20, 30)
	my_triangle.side()
	my_triangle.perimeter()
	my_triangle.area()
	my_triangle.draw()

	my_rectangle = Rectangle(60, 40)
	my_rectangle.side()
	my_rectangle.perimeter()
	my_rectangle.area()
	my_rectangle.draw()

	my_ellipse = Ellipse(50, 80)
	my_ellipse.side()
	my_ellipse.perimeter()
	my_ellipse.area()
	my_ellipse.draw()

	my_eqtr = Equilateraltriangle(60)
	my_eqtr.side()
	my_eqtr.perimeter()
	my_eqtr.area()
	my_eqtr.draw()

	my_square = Square(45)
	my_square.side()
	my_square.perimeter()
	my_square.area()
	my_square.draw()

	my_circle = Circle(30)
	my_circle.side()
	my_circle.perimeter()
	my_circle.area()
	my_circle.draw()
