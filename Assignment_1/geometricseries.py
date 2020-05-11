a = int(input("Enter first term of geometric series: "))
r = int(input("Enter the common ratio: "))
terms = []
for i in range(10):
    n = a * r**i
    terms.append(n)
print (terms)

