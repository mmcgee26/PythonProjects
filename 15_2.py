graph = {1: {2, 3}, 
        2: {1, 4},
        3: {1,5}, 
        4: {2,5,6}, 
        5: {3,4},
        6: {4,7}, 
        7: {6}}

def dfs_iterative(graph, start):    # return a DFS path
  visited = []                  # visited vertex
  stack = [start]
 
  while stack:                  # search stops when stack is empty
    vertex = stack.pop()        # pop the top element
    if vertex not in visited:   
      visited.append(vertex)
      stack.extend(graph[vertex].difference(visited)) # append un-visited neighbors
    print(stack)
 
  return visited

print(dfs_iterative(graph, 1))



def dfs_recursive(graph, vertex, path=[]): # returns a DFS path
    path = path + [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path

print(dfs_recursive(graph, 1))
