import array

# reverse an array
arr = array.array('i', [5, 2, 8, 3, 1, 2])

i = 0
j = len(arr) - 1
for val in arr:
    if i < j :
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j = j - 1
        i = i + 1
print(arr)
