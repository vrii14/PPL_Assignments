import random
bank1 = [ "Tiger", "Grass", "Goat"]
bank2 = []
boat = []
n = 0
while len(bank1) != 0:
	a =  random.randint(0, len(bank1) - 1)
	p = bank1[a]
	bank1.remove(p)
	if "Tiger" in bank1 and "Goat" in bank1:
		bank1.append(p)
		continue
	if "Goat" in bank1 and "Grass" in bank1:
		bank1.append(p)
		continue
	
	if "Tiger" in bank2 and "Goat" in bank2:
		bank1.append(bank2.pop())
		continue
	if "Goat" in bank2 and "Grass" in bank2:
		bank1.append(bank2.pop())
		continue
	bank2.append(p)
	n += 1
	print("In", n, "trip of boat man and", p)
	
