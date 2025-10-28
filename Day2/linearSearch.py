import array

arr = array.array('i',[2,5,9,3,6])

# find 9
k=9
pos =-1

for i in range(0,len(arr)):
    if arr[i]==k:
        pos = i
        break

if pos ==-1:
    print("element not found")
else:
    print("element found at position: " + str(pos+1))