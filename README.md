# **Artificial Intelligence**
## **I. Search Algorithms**
### 1. Breadth First Search
- Helping you search element according to breadth of tree
### 2. Depth First Search
- Helping you search element according to depth of tree
### 3. Uniform Cost Search
- For weighted graphs, it expect using weighted on Graph to choose a path with weighted total as minimum as posible
- BFS can find a shorter path than UCS but the weighted total always higher than UCS
- UCS priority for cost but not preference for path
- Using `f(n) = g(n)` to represent for cost from itself to its parent and select next state with value of `f(n)` is smallest

### 4. Greedy Best First Search (GBFS)
- Similar UCS but using `f(n) = h(n)` to represent for cost from itself to destination and select next state with value of `f(n)` is smallest
### 5. A-star
- Similar UCS but using `f(n) = g(n) + h(n)` to represent for cost from itself to destination and select next state with value of `f(n)` is smallest
- A-star combine UCS and GBFS 

## **II. Installation**
### 1. Breadth First Search
- Using `Queue` that operate by mechanism FIFO 

```python
def BFS(tree, name_node):
    frontier = [tree]
    explored = []
    print('BFS: ')
    while len(frontier) != 0: 
        state = frontier.pop(0)
        print(state, end=' -> ') # showing current state 
        if state.name.upper() == name_node.upper(): 
            return True
        
        explored.append(state)
        
        for node in state.neighbors():
            if node not in frontier and node not in explored:
                frontier.append(node)
    return False
```

### 2. Breadth First Search
- Using `Stack` that operate by mechanism LIFO 

```python
def DFS(tree, name_node):
    frontier = [tree]
    explored = []
    print('DFS: ')
    while len(frontier) != 0: 
        state = frontier.pop()
        print(state, end=' -> ') # showing current state 
        if state.name.upper() == name_node.upper():
            return True
        
        explored.append(state)
        
        for node in state.neighbors():
            if node not in frontier and node not in explored:
                frontier.append(node)
    return False
```
### 3. Uniform Cost Search, Greedy Best First Search, A-star
- Using `Heap` 
```python
def UCS_GBFS_Astar(root, name_node):
    frontier = [root]
    explored = []

    while len(frontier) != 0:
        state = heappop(frontier)
        print(state, end=' -> ') # showing current state 
        if state.name.upper() == name_node.upper():
            return True
        explored.append(state)

        for node in state.neighbors():
            if node not in frontier and node not in explored:
                heappush(frontier, node)
    return False
```
- Because UCS, GBFS, A* has same mechanism `Heap` so I just write only one def
- But it depends on input data to rearrange list in order to suitable with request (UCS, GBFS or A*) in `tree.py` file
```python
    # compares to sort heap list
    # value = g(n) + h(n)

    # UCS : value = g(n) && h(n) = 0
    # GBFS: value = h(n) && g(n) = 0
    # A-star : value = g(n) + h(n)
    def __lt__(self, other):
        return self.value < other.value
```

## **III. Using**

- Clone repos https://github.com/lecamit83/AI.git
- Go to folder
- Run file index 
``` bash
$ python3 index.py
```