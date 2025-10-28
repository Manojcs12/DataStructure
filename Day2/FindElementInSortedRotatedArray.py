import array

arr = array.array('i', [7, 11, 13, 17, 19, 23, 2, 3, 5])

k = 23

s = 0
e = len(arr) - 1
pos = -1
while s <= e:
    mid = int((s + e) / 2)

    if arr[mid] == k:
        pos = mid
        break

    if arr[s] < arr[mid]:
        if arr[mid] > k >= arr[s]:
            e = mid - 1
        else:
            s = mid + 1
    elif arr[mid + 1] < arr[e]:
        if arr[mid + 1] <= k <= arr[e]:
            s = mid + 1
        else:
            e = mid - 1

print(pos)
