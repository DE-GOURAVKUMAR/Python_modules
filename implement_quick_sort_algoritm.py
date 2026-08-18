# in this program it will sort the orignal list or array
def quick_sort(num_list):
    arr = num_list
    if arr == []:
        return []
    low = 0    
    high = len(arr) - 1
    qs_helper(arr, low, high)
    return arr
def qs_helper(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        left = qs_helper(arr, low, p-1)
        right = qs_helper(arr, p+1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while (i < j and arr[i] < pivot):
            i += 1
        while (i <= j and arr[j] > pivot):
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

num = [20,2,14,1,5]
print(quick_sort(num))
print(num)


