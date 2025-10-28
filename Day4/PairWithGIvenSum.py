# Python3 implementation of simple method to
# find count of pairs with given sum.

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'


def printPairs(arr, n, sum):
    # Store counts of all elements
    # in a dictionary
    mydict = dict()

    # Traverse through all the elements
    for i in range(n):

        # Search if a pair can be
        # formed with arr[i]
        temp = sum - arr[i]

        if temp in mydict:
            count = mydict[temp]
            for j in range(count):
                print("(", temp, ", ", arr[i],
                      ")", sep="", end='\n')

        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1


# Driver code
if __name__ == '__main__':
    arr = [5, 1, 3, 8, -2, 10, 17, 9, 7]
    n = len(arr)
    sum = 8

    printPairs(arr, n, sum)
