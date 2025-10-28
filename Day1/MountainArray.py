import array

arr = array.array('i', [6,7,7,8,6])

isMountain = True
if len(arr) < 3:
    isMountain = False
else:
    i = 1
    j = 1
    mountain = arr[0]
    mountainIndex = 0
    for i in range(i, len(arr)-1):
        if arr[i] > mountain:
            mountain = arr[i]
            mountainIndex = i
    if mountainIndex == (len(arr)-1) or mountainIndex ==0:
        isMountain = False
    if(isMountain):
        maxNum = mountain
        for j in range(mountainIndex + 1, len(arr)):
            if arr[j] >= maxNum:
                isMountain = False
                break
            maxNum = arr[j]
        maxNum = arr[0]
        for j in range(1, mountainIndex):
            if arr[j] <= maxNum:
                isMountain = False
                break
            maxNum = arr[j]
print("Is given array mountain :" + str(isMountain))
