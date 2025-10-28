import array

arr = array.array('i', [1, 3, 5, 7, 9, 2])

# WAP to rotate an array k times
k = 2
i = 0
j = len(arr) - k - 1
# reverse first part till k
while (i < j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i = i + 1
    j = j - 1
i = len(arr) - k
j = len(arr) - 1
# reverse last part from k to len of arr
while (i < j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    j = j - 1

# reverse full array
i = 0
j = len(arr) - 1
for val in arr:
    if i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j = j - 1
        i = i + 1
print(arr)
