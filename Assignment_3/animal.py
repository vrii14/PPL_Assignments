

class Cat:

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

my_cat = Cat("Misty", 25)
my_cat.name()
my_cat.age()
my_cat.eat()
my_cat.speak()


class Dog:

	def __init__(self, dname = "Ronny", age = 30):
		self.__dname = dname
		self.__dage = dage


	def __name(self):
		print("I am a dog and my name is {}".format(self.__kname))

	def __age(self):
		print("My age is {}".format(self.__kage))


	def accessname(self):
		self.__name()

	def accessage(self):
		self.__age()


	def eat(self):
		print("I eat raw meat, bones, organs and a small amount of the vegetable.")

	def speak(self):
		print("Bhow Bhow!")

my_dog = Dog("Tammy", 26)
my_dog.accessname()
my_dog.accessage()
my_dog.eat()
my_dog.speak()


class Lion:

	def __init__(self, lname = "Simba", lage = 35):
		self.__lname = lname
		self.lage = lage


	def __name(self):
		print("I am a lion and my name is {}".format(self.lname))

	def age(self):
		print("My age is {}".format(self.lage))

	def accessname(self):
		self.__name()


	def eat(self):
		print("I eat meat.")

	def speak(self):
		print("I roarr.")


my_lion = Lion("Raja", 38)
my_lion.accessname()
my_lion.age()
my_lion.eat()
my_lion.speak()



class Zebra:

	def __init__(zname = "Zed", zage = 28):
		self.zname = zname
		self.__zage = zage

	def name(self):
		print("I am a Zebra and my name is {}".format(self.zname))

	def __age(self):
		print("My age is {}".format(__zage))

	def accessage(self):
		self.__age()


	def eat(self):
		print("I eat grass, herbs and shrubs.")

	def speak(self):
		print("I either bark, bray or snort.")


my_zebra = Zebra("Zenny", 20)
my_zebra.name()
my_zebra.accessage()
my_zebra.eat()
my_zebra.speak()



class Bear:

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


my_bear = Bear("Fuzzy", 45)
my_bear.name()
my_bear.age()
my_bear.eat()
my_bear.speak()



class Deer:

	def __init__(self, dename = "Bobby", deage = 30):
		self.__dename = dename
		self.__deage = deage

	def __name(self):
		print("I am a deer and my name is {}".format(self.__dename))


	def __age(self):
		print("My age is {}".format(self.__deage))

	def accessname(self):
		self.__name()

	def accessage(self):
		self.__age()


	def eat(self):
		print("I eat grass, bark, twigs, berries, young shoots and other vegetation.")

	def speak(self):
		print("I make a loud grunting sound.")


my_deer = Deer("Bucky", 29)
my_deer.accessname()
my_deer.accessage()
my_deer.eat()
my_deer.speak()


class Giraffe:

	def __init__(self, gname = "Noah", gage = 40):
		self.gname = gname
		self.gage  = gage


	def name(self):
		print("I am a Giraffe and my name is {}".format(self.gname))

	def age(self):
		print("My age is {}".format(self.gage))


	def eat(self):
		print("I eat  eat the leaves and twigs of acacia, mimosa, and wild apricot trees.")

	def speak(self):
		print("I hum.")

my_giraffe = Giraffe("Apollo", 37)
my_giraffe.name()
my_giraffe.age()
my_giraffe.eat()
my_giraffe.speak()



class Cow:

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


my_cow = Cow("Emma", 36)
my_cow.name()
my_cow.age()
my_cow.eat()
my_cow.speak()
