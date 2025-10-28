import array

# push all zeroes to the end of array
arr = array.array('i', [5, 0, 8, 9, 0, 3, 0, 2])

index = 0
j = 0
for i in arr:
    if i != 0:
        temp = arr[j]
        arr[j] = arr[index]
        arr[index] = temp
        j = j+1
    index = index + 1
print(arr)
