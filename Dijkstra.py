def main():
    x = 1
    #nodes 
    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    
    #edges/weights 
    distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

    unvisited = {node: None for node in nodes} #using None as +inf
    #set of visited nodes 
    visited = {}
    #Starting Point
    current = 'B'
    
    #Initialize-Single Source
    #Distance starts at zero
    currentDistance = 0
    unvisited[current] = currentDistance

    #While graph is not empty and while explore nodes does not equal set of nodes V 
    while True:
        #Select a node v not in S with at least one edge from visited for which...
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            #...d'(v) = min + edge is as small as possible 
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        #Add v to visited and define d(v) = d'(v) (Relax) 
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    print(visited)
    

main()

    #Relate Shortest Path to Cache
    #Dijkstra and Cache both avoid the farthest/most expensive edge

    #Proof that the code terminates with Pu is shortest s-u path
    #For size of 1, shortest path is zero which is optimal
    #For size n+1, Dijkstra takes orginal path to get to "added" node
    #So the path is at least as long has orginal path from inudction hypothesis
    
    #Proof that the code runs in o(mlogn) time
    #The code has to go through all nodes (m) and to find each edge in hashmap its logn
