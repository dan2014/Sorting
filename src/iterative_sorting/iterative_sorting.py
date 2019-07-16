# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if(arr[j] < arr[smallest_index]):
                smallest_index = j

        # TO-DO: swap
        arr[i],arr[smallest_index] = arr[smallest_index],arr[i]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    passes = 0
    while(passes <= len(arr)):
        for i in range(len(arr)-1) :
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1],arr[i]
                passes = 0
            else:
                passes += 1

    return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


if __name__ == "__main__":
    print(selection_sort([6,5,3,1,8,7,2,4]))