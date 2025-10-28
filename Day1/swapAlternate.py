import array
# swap 0th with 1th ,2th wid 3rd ......
arr = array.array('i', [4, 12, 8, -3, 12, 16, 20, 10, 1, 3])
index = 0
for i in arr:
    if index < len(arr):
        temp = arr[index]
        if (index+1) < len(arr):
            arr[index] = arr[index + 1]
            arr[index + 1] = temp
        index = index + 2
print(arr)