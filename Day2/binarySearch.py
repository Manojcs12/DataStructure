import array

# Array must be sorted.

arr = array.array('i', [2, 3, 5, 7, 11, 13, 17, 19])

k = 20
pos =-1
start =0
end = len(arr)-1
while start <= end:
    mid = int((start +end )/ 2)
    if arr[mid] == k:
        print("Element found at position:" + str(mid+1))
        pos = mid
        break
    if arr[mid]< k :
        start = mid+1
    else:
        end = mid-1

if pos == -1:
    print("element not found")





