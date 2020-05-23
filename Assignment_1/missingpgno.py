p = input("Enter the page numbers present in the book\n")
p = set(p.split(","))
p = {int(n) for n in p}
check = set(range(1,25))
print("Missing page numbers are:- \n")
print(check - p)
