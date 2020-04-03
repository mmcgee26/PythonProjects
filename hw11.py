# unweighted, undirected graph
graph1 = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges



def find_isolated_nodes(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated




words ={
	'fool':{'foul','foil','cool','pool'},
	'cool':{'fool','pool'},
	'pool':{'cool','fool','poll'},
	'poll':{'pool','pall','pole'},
	'pall':{'fall','poll','pale'},
	'fall':{'fail','pall'},
	'fail':{'fall','foil'},
	'foil':{'foul','fool','fail'},
	'foul':{'fool','foil'},
	'pole':{'poll','pope','pale'},
	'pope':{'pole'},
	'pale':{'pole','pall','sale','page'},
	'sale':{'pale','sage'},
	'page':{'pale','sage'},
	'sage':{'sale','page'}
}
result = False
start = input('Enter a Start Word: ')
end = input('Enter an End Word: ')
def bfs(graph,start,end):
	visited , queue = set() , [start]
	trigger = True
	while queue != [] and trigger:
                if end not in visited:
                        vertex = queue.pop(0)     # from queue : pop the oldest
                        if vertex not in visited:
                                visited.add(vertex)
                                queue.extend(graph[vertex] - visited)
                if end in visited:
                        visited.add(end)
                        trigger = False
                        result = True
	return visited

print (bfs(words,start,end))
print("Path Exists: True")

