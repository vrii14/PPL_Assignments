pages = [2, 4, 5, 6, 12, 16, 17, 21, 20]
pages.sort()
#print (pages)
for i in range(1,26):
    if(i not in pages):
        print(f"{i} is missing page number.")


