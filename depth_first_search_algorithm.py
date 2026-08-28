def dfs(matrix, n):
    visited = []
    stack = [n]
    
    
    for index in range(n, len(matrix)):
        while stack:
            l = len(stack) - 1
            if stack[l] not in visited:
                node = stack.pop()
                visited.append(node)
        col = []        
        for i in range(len(matrix[index])):
            if matrix[index][i] == 1:
                col.append(i)
                
                
                if i not in visited:
                    stack.insert(0, i)
         
            
    return visited

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))