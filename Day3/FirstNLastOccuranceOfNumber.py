import array

# https://www.youtube.com/watch?v=_VCaXbncyeQ


# given a sorted array of elements ,find the first and last occurrence of number
# k=2
arr = array.array('i', [1, 1, 2, 2, 2, 2, 3, 7, 8, 8])

k = 1
pos = -1
start = 0
end = len(arr) - 1
lastcflag = True
firstcflag = True
while start <= end:
    mid = int((start + end) / 2)
    if arr[mid] == k:
        print("Element found at position:" + str(mid + 1))
        pos = mid
        break
    if arr[mid] < k:
        start = mid + 1
    else:
        end = mid - 1

if pos == -1:
    print("element not found")
else:
    last_pos = pos
    while lastcflag:
        if last_pos != end and arr[last_pos + 1] == arr[last_pos]:
            last_pos = last_pos + 1
        else:
            lastcflag = False
    first_pos = pos
    while firstcflag:
        if first_pos != end and arr[first_pos - 1] == arr[first_pos]:
            first_pos = first_pos - 1
        else:
            firstcflag = False

print("Last position:" + str(last_pos + 1))
print("First position:" + str(first_pos + 1))


# Bhaiya's prog using binary
def findFirstOccurance(arr, k):
    first = 0
    last = len(arr) - 1
    fo = -1
    while (first <= last):
        mid = int((first + last) / 2)
        if arr[mid] == k:
            fo = mid
            last = mid - 1
        elif arr[mid] > k:
            last = mid - 1
        else:
            first = mid + 1

    print("First position:" + str(fo + 1))

def findLastOccurance(arr, k):
    first = 0
    last = len(arr) - 1
    lo = -1
    while (first <= last):
        mid = int((first + last) / 2)
        if arr[mid] == k:
            lo = mid
            first = mid + 1
        elif arr[mid] > k:
            last = mid - 1
        else:
            first = mid + 1

    print("Last position:" + str(lo + 1))
