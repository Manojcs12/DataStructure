# find the square root of the number w/o using sqrt to nearest integer

k = 27

start = 0
end = 27
result = 0
while start <= end:
    mid = int((start + end) / 2)
    if mid * mid == k:
        result = mid
        break
    elif mid * mid > k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)