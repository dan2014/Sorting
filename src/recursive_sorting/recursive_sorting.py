import math

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arrA_index = 0
    arrB_index = 0
    for i in range(0,elements):
        if(arrA_index == len(arrA) or arrB_index == len(arrB)):
            if(arrA_index == len(arrA)):
                merged_arr[i] =  arrB[arrB_index]
                arrB_index += 1
            else:
                merged_arr[i] =  arrA[arrA_index]
                arrA_index += 1
        else:
            if(arrA_index < len(arrA) and arrA[arrA_index] <= arrB[arrB_index]):
                merged_arr[i] =  arrA[arrA_index]
                arrA_index += 1
            else: 
                merged_arr[i] =  arrB[arrB_index]
                arrB_index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if(len(arr) == 1 or len(arr) == 0):
        return arr
    
    if(len(arr)%2 == 0):
        left_slice = len(arr)//2
        right_slice = len(arr) - left_slice
    else:
        left_slice = len(arr)//2 + 1
        right_slice = len(arr) - left_slice + 1
    left = merge_sort(arr[:left_slice])
    right = merge_sort(arr[right_slice:])
    merged = merge(left,right)

    return merged


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


if(__name__ == "__main__"):
    print(merge_sort([5,8,3,7,4,1,2,6]))