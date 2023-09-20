def count_zeros(arr):
    # If the length of the array is 1, it checks whether the single element is a zero or not, 
    # and returns 1 if it is, or 0 if it's not.
    if len(arr) == 1:
        if arr[0] == 0:
            return 1  
        else:
            return 0
    # finding the mid element.
    mid = len(arr) // 2
    #dividing the array into two equal half.
    # creating first arr starting from start to mid.
    left_half = arr[:mid]
    # creating second arr starting from mid to last.
    right_half = arr[mid:]
    
    # now recursively calling the count_zeros funtion with left array as an input.
    # to count no of zero in left array
    left_count = count_zeros(left_half)
    # again now recursively calling the count_zeros funtion with right array as an input.
    # to count no of zero in right array
    right_count = count_zeros(right_half)
    # just returning now the sum of count of 0 in left array and right array.
    return left_count + right_count
#giving input
arr = [1, 0, 1, 0, 1, 0, 1, 0, 0]
result = count_zeros(arr)
print('The number of zeros in the given array is:' ,result)
