import array

arr = array.array('i', [7, 5, 8, 9, 2])

i = 0
maxNum = arr[0]
count = 1
for val in arr:
    if val > maxNum:
        maxNum = val
        i = i + 1
        count = count + 1
print(count)
