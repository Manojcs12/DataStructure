import array

# find smallest number with position in array
arr = array.array('i', [12, 17, 11, 19, 16, 13])
pos = 0
smallestNumber = arr[0]
index = 0
for i in arr:
    if i < smallestNumber:
        smallestNumber = i
        pos = index + 1
    index = index + 1

print(smallestNumber)
print(pos)
