from tree import Node
import searching


def BFS_and_DFS() : 
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')
    j = Node('J')
    k = Node('K')
    l = Node('L')
    m = Node('M')
    n = Node('N') 
    o = Node('O')
    
    h.append(n, o)
    f.append(k, l, m)
    b.append(e, f)
    c.append(g, h)
    d.append(i, j)
    a.append(b, c, d)
    tree_structure = """

    root A
    |___B
    |   |__E
    |   |___F
    |       |__K
    |       |__L
    |       |__M
    |
    |___C
    |   |__G
    |   |___H
    |       |__N
    |       |__O
    |
    |___D
        |__I
        |__J
    
    """
    print(tree_structure)
    print('--'*30)
    print(searching.BFS(a, 'N'))
    print('--'*30)
    print(searching.DFS(a, 'N'))
    print('--'*30)

def UCS():
    a = Node('A', length_from_itself_to_parent=6)
    b = Node('B', length_from_itself_to_parent=3)
    c = Node('C', length_from_itself_to_parent=4)
    d = Node('D', length_from_itself_to_parent=5)
    e = Node('E', length_from_itself_to_parent=3)
    f = Node('F', length_from_itself_to_parent=1)
    g = Node('G', length_from_itself_to_parent=6)
    h = Node('H', length_from_itself_to_parent=2)
    i = Node('I', length_from_itself_to_parent=5)
    j = Node('J', length_from_itself_to_parent=4)
    k = Node('K', length_from_itself_to_parent=2)
    l = Node('L', length_from_itself_to_parent=0)
    m = Node('M', length_from_itself_to_parent=4)
    n = Node('N', length_from_itself_to_parent=0) 
    o = Node('O', length_from_itself_to_parent=4)
    
    h.append(n, o)
    f.append(k, l, m)
    b.append(e, f)
    c.append(g, h)
    d.append(i, j)
    a.append(b, c, d)
   
    tree_structure = """
    
    root A(6) 
    |___B(3)
    |   |__E(3)
    |   |___F(1)
    |       |__K(2)
    |       |__L(0)
    |       |__M(4)
    |
    |___C(4)
    |   |__G(6)
    |   |___H(2)
    |       |__N(0)
    |       |__O(4)
    |
    |___D(5)
        |__I(5)
        |__J(4)
    
    """
    print(tree_structure)

    print('--'*30)
    print(UCS)
    print(searching.UCS_GBFS_Astar(a, 'N'))
    print('--'*30)

def UCS():
    a = Node('A', length_from_itself_to_parent=0)
    b = Node('B', length_from_itself_to_parent=2)
    c = Node('C', length_from_itself_to_parent=1)
    d = Node('D', length_from_itself_to_parent=3)
    e = Node('E', length_from_itself_to_parent=5)
    f = Node('F', length_from_itself_to_parent=4)
    g = Node('G', length_from_itself_to_parent=6)
    h = Node('H', length_from_itself_to_parent=3)
    i = Node('I', length_from_itself_to_parent=2)
    j = Node('J', length_from_itself_to_parent=4)
    k = Node('K', length_from_itself_to_parent=2)
    l = Node('L', length_from_itself_to_parent=1)
    m = Node('M', length_from_itself_to_parent=4)
    n = Node('N', length_from_itself_to_parent=2) 
    o = Node('O', length_from_itself_to_parent=4)
    
    h.append(n, o)
    f.append(k, l, m)
    b.append(e, f)
    c.append(g, h)
    d.append(i, j)
    a.append(b, c, d)
   
    tree_structure = """
   
    root A(0) 
    |___B(2)
    |   |__E(5)
    |   |___F(4)
    |       |__K(2)
    |       |__L(1)
    |       |__M(4)
    |
    |___C(1)
    |   |__G(6)
    |   |___H(3)
    |       |__N(2)
    |       |__O(4)
    |
    |___D(3)
        |__I(2)
        |__J(4)
    
    """
    print(tree_structure)

    print('--'*30)
    print('UCS : ')
    print(searching.UCS_GBFS_Astar(a, 'N'))
    print('--'*30)

def GBFS():
    a = Node('A', length_to_dest=6)
    b = Node('B', length_to_dest=3)
    c = Node('C', length_to_dest=4)
    d = Node('D', length_to_dest=5)
    e = Node('E', length_to_dest=3)
    f = Node('F', length_to_dest=1)
    g = Node('G', length_to_dest=6)
    h = Node('H', length_to_dest=2)
    i = Node('I', length_to_dest=5)
    j = Node('J', length_to_dest=4)
    k = Node('K', length_to_dest=2)
    l = Node('L', length_to_dest=0)
    m = Node('M', length_to_dest=4)
    n = Node('N', length_to_dest=0) 
    o = Node('O', length_to_dest=4)
    
    h.append(n, o)
    f.append(k, l, m)
    b.append(e, f)
    c.append(g, h)
    d.append(i, j)
    a.append(b, c, d)
   
    tree_structure = """
    
    root A(6) 
    |___B(3)
    |   |__E(3)
    |   |___F(1)
    |       |__K(2)
    |       |__L(0)
    |       |__M(4)
    |
    |___C(4)
    |   |__G(6)
    |   |___H(2)
    |       |__N(0)
    |       |__O(4)
    |
    |___D(5)
        |__I(5)
        |__J(4)
    
    """
    print(tree_structure)

    print('--'*30)
    print('GBFS : ')
    print(searching.UCS_GBFS_Astar(a, 'N'))
    print('--'*30)

def Astar() : 
    a = Node('A', length_to_dest=6, length_from_itself_to_parent=0)
    b = Node('B', length_to_dest=3, length_from_itself_to_parent=2)
    c = Node('C', length_to_dest=4, length_from_itself_to_parent=1)
    d = Node('D', length_to_dest=5, length_from_itself_to_parent=3)
    e = Node('E', length_to_dest=3, length_from_itself_to_parent=5)
    f = Node('F', length_to_dest=1, length_from_itself_to_parent=4)
    g = Node('G', length_to_dest=6, length_from_itself_to_parent=6)
    h = Node('H', length_to_dest=2, length_from_itself_to_parent=3)
    i = Node('I', length_to_dest=5, length_from_itself_to_parent=2)
    j = Node('J', length_to_dest=4, length_from_itself_to_parent=4)
    k = Node('K', length_to_dest=2, length_from_itself_to_parent=2)
    l = Node('L', length_to_dest=0, length_from_itself_to_parent=1)
    m = Node('M', length_to_dest=4, length_from_itself_to_parent=4)
    n = Node('N', length_to_dest=0, length_from_itself_to_parent=2) 
    o = Node('O', length_to_dest=4, length_from_itself_to_parent=4)
    
    h.append(n, o)
    f.append(k, l, m)
    b.append(e, f)
    c.append(g, h)
    d.append(i, j)
    a.append(b, c, d)
    
    tree_structure = """
    A* :
    root A(6)(0) 
    |___B(3)(2)
    |   |__E(3)(5)
    |   |___F(1)(4)
    |       |__K(2)(2)
    |       |__L(0)(1)
    |       |__M(4)(4)
    |
    |___C(4)(1)
    |   |__G(6)(6)
    |   |___H(2)(3)
    |       |__N(0)(2)
    |       |__O(4)(4)
    |
    |___D(5)(3)
        |__I(5)(2)
        |__J(4)(4)
    
    """
    print(tree_structure)

    print('--'*30)
    print('A* : ')
    print(searching.UCS_GBFS_Astar(a, 'N'))
    print('--'*30)


if __name__ == "__main__":
    # BFS_and_DFS()
    # UCS()
    GBFS()
    # Astar()
