class Node():
    def __init__(self, name = ''):
        self.name = name
        self.connections = []
        self.visited = False

def recursive(x):
    if x > 10:
        return
    print(x)
    recursive(x+1)

def parse_tree(node):
    # this depth first search ACTUALLY WORKS
    visited_list.append(node)
    #print(f'{node.name}:')
    for connection in node.connections:
            print(f'{node.name}:')
            print(f'connection: {connection.name}')
            parse_tree(connection)

if __name__ == "__main__":
    #x = 0
    #recursive(x)
    node_a = Node(name='node_a')
    node_b = Node(name='node_b')
    node_c = Node(name='node_c')
    node_d = Node(name='node_d')
    node_a.connections.append(node_b)
    node_a.connections.append(node_d)
    node_b.connections.append(node_c)
    #node_b.connections.append(node_d)

    visited_list =[]
    parse_tree(node_a)
    print('visited:')
    for node in visited_list:
         print(node.name)
    #print(visited_list)