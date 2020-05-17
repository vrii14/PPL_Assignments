'''
	In this implementation of classes Animal is the parent class and inherits all the other classes. It contains the abstract methods which are defined in the
    child classes. The flow is as follows:
    1. Animal is the base class
    2. Herbivore, Carnivore and Omnivore are derived classes of Animal class.
    3. Deer and Cow are derived classes of Herbivore class.
    4. Cat and Lion are derived classes of Carnivore class.
    5. Bear and Human are derived classes of Omnivore class.
    At the end all the methods are called by creating objects of respecting classes.
'''

from abc import ABC,abstractmethod

class Animal(ABC):

	def animal(self):
		print("I am an animal.")

	@abstractmethod
	def name(self):
		pass

	@abstractmethod
	def age(self):
		pass

	@abstractmethod
	def eat(self):
		pass

	@abstractmethod
	def speak(self):
		pass



class Herbivore(Animal):

	def eat(self):
		print("I eat plant material.")



class Carnivore(Animal):

 	def eat(self):
 		print("I eat other animals.")


class Omnivore(Animal):

 	def eat(self):
 		print("I eat both plant material and meat.")


class Deer(Herbivore):

	def __init__(self, dname = "Bobby", dage = 30):
		self.dname = dname
		self.dage = dage

	def name(self):
		print("I am a deer and my name is {}".format(self.dname))


	def age(self):
		print("My age is {}".format(self.dage))


	def eat(self):
		print("I eat grass, bark, twigs, berries, young shoots and other vegetation.")

	def speak(self):
		print("I make a loud grunting sound.")



class Cow(Herbivore):

	def __init__(self, cname = "Molly", cage = 25):
		self.cname = cname
		self.cage = cage


	def name(self):
		print("I am a cow and my name is {}".format(self.cname))

	def age(self):
		print("I am {} years old.".format(self.cage))

	def eat(self):
		print("I eat grass and grains.")

	def speak(self):
		print("Mooo Mooo!")


class Cat(Carnivore):

	def __init__(self, kname = "Kitty", kage = 20):
		self.kname = kname
		self.kage = kage


	def name(self):
		print("I am a cat and my name is {}".format(self.kname))

	def age(self):
		print("My age is {}".format(self.kage))


	def eat(self):
		print("I eat cooked beef, chicken and turkey.")

	def speak(self):
		print("Meow Meow!")


class Lion(Carnivore):

	def __init__(self, lname = "Shersingh", lage = 30):
		self.lname = lname
		self.lage = lage


	def name(self):
		print("I am a lion and my name is {}".format(self.lname))

	def age(self):
		print("My age is {}".format(self.lage))


	def eat(self):
		print("I eat meat.")

	def speak(self):
		print("I roarr.")


class Bear(Omnivore):

	def __init__(self, bname = "Teddy", bage = 40):
		self.bname = bname
		self.bage = bage


	def name(self):
		print("I am a bear and my name is {}".format(self.bname))

	def age(self):
		print("My age is {}".format(self.bage))


	def eat(self):
		print("I eat plants, insects, fish, and animals.")

	def speak(self):
		print("I growl.")


class Human(Omnivore):

	def __init__(self, hname = "Ram", hage = 30):
		self.hname = hname
		self.hage = hage


	def name(self):
		print("I am a human and my name is {}".format(self.hname))

	def age(self):
		print("My age is {}".format(self.hage))


	def eat(self):
		print("I eat vegetables and meat.")

	def speak(self):
		print("I talk a lot and can speak everything!")



if __name__ == '__main__':
	
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

