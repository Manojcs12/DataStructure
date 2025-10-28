import array

arr = array.array('i', [1, 2, 3, 4, 5, 2])
# naive approach
for i in range(0, len(arr)):
    maxNum = arr[i]
    isLeader = True
    for j in range(i, len(arr)):
        if maxNum < arr[j]:
            isLeader = False
            break

    if isLeader:
        print(arr[i])

# another approach
l = len(arr)
max_from_right = arr[l - 1]
print("------")
for i in range(l - 2, -1, -1):
    if max_from_right < arr[i]:
        print(max_from_right)
        max_from_right = arr[i]
print(max_from_right)