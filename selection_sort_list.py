def selection_sort(list_of_num):
    length = len(list_of_num)
    for i in range(length):
        min_num = i
        for j in range(min_num, length):
            if list_of_num[min_num] > list_of_num[j]:
                min_num = j
        if list_of_num[i] == list_of_num[min_num]:
            list_of_num[i]
        else:
            list_of_num[i], list_of_num[min_num] = list_of_num[min_num], list_of_num[i]

    return list_of_num

print(selection_sort([12, 2, 31, 51, 99, 22, 33, 976, 44, 67]))