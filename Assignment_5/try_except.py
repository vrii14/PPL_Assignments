#Exception for ZeroDivision Error

print("Enter the values for a and b for division of a by b")
a = int(input())
b = int(input())
try:
	print(a/b)
except ZeroDivisionError:
	print("Zero Division Error:- A number cannot be divided by zero\n")



#Type error 
#Since the input is of type string and we need it to be integer

print("Enter a numeric string")
a = input()
try:
	print(a/3)
except TypeError:
	print("A string cannot be divided by a integer. Convert the type of string to integer\n")



#If you don't know which type of exception to raise, then don't specify the exception name
def fileopen():
	while True:
		print("Enter a file you want to read")
		a = input()
		try:
			f = open(a, "r")
			m = f.read()
			print("This is the content of your file")
			print(m)
		except:
			print("This file is not present in the current directory")
			continue
		else:
			break

fileopen()

#Error when do not have a some permissions for the files (IO exception)

try:
	f = open('test.txt','r')
	f.write('Test write this')
except IOError:
	print("\nError: Could not find file or read data\n")
else:
	print("Content written successfully")
	f.close() 




#We can also raise a exception in python using raise keyword

print("I am trying to raise my exception")
try:
	raise Myerror("I deliberately raised this exception")
except:
	print("Myerror is not a defined exception\n")




#we can also create functions using try except block. And it will run until user provides the expected input

def ask():
	
	while True:
		try:
			n = int(input('Input an integer: '))
		except:
			print('An error occurred! Please try again!')
			continue
		else:
			break
			
		
	print('Thank you, your number squared is: ',n**2)

ask()
