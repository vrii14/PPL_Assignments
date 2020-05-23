In this assignment we made classes of animals and shapes and then instantiated them. 
A lot of OOP concepts were used in this assignment like:
1. Virtual function :- It is defined in the base class and then redifined in the derived class with a different functionality. Usually
in the base class only the function is defined with no functionality(pass keyword) and defined in the derived classes.
2. Abstract Classes :- It is the class which contains two or more abstract methods which mean that they generally don't have implementation
in this class and the subclass inheriting the abstract class provides the implementation. The abstract class cannot be instantiated i.e., no
objects can be formed. Its basically derived from ABC class and for specifying an abstract method @abstractmethod is used.
3. Polymorphism :- It means the same function names are used but with different implementation in different derived classes. Some examples 
from the assignment include the area, perimeter and draw methods in shapes.
4. Building a hierachy in the classes using parent class and child classes and continuing doing so. Like
Shape -> Polygon -> Triangle -> Equilateral Triangle.
5. Modularity :- It means making multiple modules first and then linking them to form a complete system. It minimises the duplication. I used modularity by importing all classes of animals and shapes into one file and creatted objects and called methods in this file.
