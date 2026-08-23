def adjacency_list_to_matrix(lists: dict):
    matrix = []
    no_of_nodes = len(lists)

    for value in lists.values():
        out_l = [0 for i in range(no_of_nodes)]
        for a in range(no_of_nodes):
            if a in value:
                out_l[a] = 1
            else:
                out_l[a] = 0
        matrix.append(out_l)
        print(out_l)
    return matrix 

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})