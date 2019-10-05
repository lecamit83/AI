class Node:
    def __init__(self, name = '', length_to_dest = 0, length_from_itself_to_parent = 0):
        self.name = name
        self.value = length_to_dest + length_from_itself_to_parent
        self.childrens = []

    def __str__(self):
        return self.name

    def append(self, *nodes):
        for node in nodes:      
            self.childrens.append(node)
    
    def neighbors(self):
        return self.childrens
        
    # compares the second value
    def __lt__(self, other):
        return self.value < other.value
