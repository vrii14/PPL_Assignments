n1 = int(input("Enter starting number of the range: "))
print(type(n1))
n2 = int(input("Enter last number in the range: "))
armstrong = []
for i in range(n1, n2+1):
    number = [int(d) for d in str(i)]
    #print (number)
    sum = 0
    for j in number:
        sum = sum + j**3
    if sum == i:
        armstrong.append(i)
print (armstrong)

