from tree import Node
from heapq import heappush, heappop

def BFS(tree, name_node):
    frontier = [tree]
    explored = []
    print('BFS: ')
    while len(frontier) != 0: 
        state = frontier.pop(0)
        print(state, end=' -> ')
        if state.name.upper() == name_node.upper():
            return True
        
        explored.append(state)
        
        for node in state.neighbors():
            if node not in frontier and node not in explored:
                frontier.append(node)
    return False

def DFS(tree, name_node):
    frontier = [tree]
    explored = []
    print('DFS: ')
    while len(frontier) != 0: 
        state = frontier.pop()
        print(state, end=' -> ')    
        if state.name.upper() == name_node.upper():
            return True
        
        explored.append(state)
        
        for node in state.neighbors():
            if node not in frontier and node not in explored:
                frontier.append(node)
    return False

def DLS(root, name_node, limited = 3):

    pass

def UCS_GBFS_Astar(root, name_node):
    frontier = [root]
    # print(frontier)
    explored = []

    while len(frontier) != 0:
        state = heappop(frontier)
        print(state, end=' -> ')
        if state.name.upper() == name_node.upper():
            return True
        explored.append(state)

        for node in state.neighbors():
            if node not in frontier and node not in explored:
                heappush(frontier, node)
    return False

