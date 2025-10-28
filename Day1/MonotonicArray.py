# Monotonic array : Strictly asc or dsc

import array

arr = array.array('i', [1,2,3,7])

i = 0
j = 1
isAsc = True
for x in range(len(arr)-1):
    if arr[i]> arr[i+1]:
        isAsc = False
        break
    i = i+1
i =0
isDsc = True
for x in range(len(arr)-1):
    if arr[i]< arr[i+1]:
        isDsc = False
        break
    i = i+1

if isAsc or isDsc:
    print("monotonic")
else:
    print("not monotonic")
