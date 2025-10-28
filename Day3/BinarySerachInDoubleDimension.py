import array

arr=[[2,4,6,8],[10,15,20,30],[40,50,55,60]]

no_of_row = len(arr)
no_of_col = len(arr[0])
k =30
print(no_of_row)
print(no_of_col)

first =0
last = no_of_row*no_of_col-1

while(first<=last):
    mid = (first+last)/2
    if arr[int(mid/no_of_col)][int(mid%no_of_col)] == k:
        posr = int(mid/no_of_col)
        posc = int(mid%no_of_col)
    elif arr[int(mid/no_of_col)][int(mid%no_of_col)] > k:
        last = mid-1
    else:
        first = mid+1


