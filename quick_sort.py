# this program will not effect the orignal list or array
def quick_sort(arr):
    if arr == []:
        return []
    
    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

num = [20,2,14,1,5]
print(quick_sort(num))
print(num)