
a ={5,2,3,1,4}

a1 = {5,1,2,9}

# find if a1 is a subset of a

count = 0
for val in a1:
    if val in a:
        count = count+1
    else:
        count = 0
        break

if count == 0:
    print("not subset")
else:
    print("subset")