import array

# Each page is allocated to student
# Each Student is allocated a page
# The maximum no. of pages allocated to student is minimum
# allocation must be continious

pages = [10, 20, 30, 40]

no_of_student = 2

first = 0

sum = 0

for val in pages:
    sum = sum + val

last = sum


def is_possible(pages, mid, no_of_student):
    count = 1
    sum = 0

    for val in pages:

        if sum + val <= mid:
            sum = sum + val
        else:
            count = count + 1
            if count > no_of_student:
                return False
            else:
                sum = val
    return True


ans = -1
while first <= last:
    mid = int((first + last) / 2)
    if is_possible(pages, mid, no_of_student):
        ans = mid
        last = mid - 1
    else:
        first = mid + 1

print(ans)
