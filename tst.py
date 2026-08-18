def selection_sort(arr):
    sorted_list = []
    if arr ==[]:
        return []
    a = min(arr)
    ind = arr.index(a)

    if min(arr) == arr[0]:
        sorted_list.append(arr[0])
    else:
        
        i = 0
        arr[i], arr[ind] = arr[ind], arr[i]
        sorted_list.append(arr[i])
        i += 1
        right = arr[i:]
        selection_sort(right) 

    return arr

print(selection_sort([20,11,100,50,90,12]))