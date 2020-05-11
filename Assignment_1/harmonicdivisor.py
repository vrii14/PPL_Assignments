n = 1
count = 0
harmondivisor = []
while count!=8:
    divisor = []
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    #print(divisor)
    for i in divisor:
        sum += 1/i
    harmonicsum = len(divisor)/sum
    if(harmonicsum.is_integer() == True):
        #print("It is a harmonic divisor number")
        harmondivisor.append(n)
        count += 1
        n+=1
    else:
            #print("It is not a harmonic divisor number")    
        n+=1
print (f"The list of harmonic divisor numbers are {harmondivisor}")
