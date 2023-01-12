''' Find a node's name from it's number '''
def find_node_name(node_number) :
    root_node = 1
    # Decide which root to start at
    with open("root_nodes_index.csv", "r") as root_nodes:
        # Find the biggest root node which is not bigger than node_number
        # This will be the root the node_number belongs to
        for node in root_nodes:
            if int(node.split(",")[1]) < node_number:
                root_node = int(node.split(",")[1])

    # Find node in main_data.csv
    with open("main_data.csv", "r") as main_data:
        nodes = main_data.readlines()
        return nodes[node_number-1].split(",")[0]

''' List all the children of a node'''
def list_children_of_node(node_number) :
    root_node = 1
    # Decide which root to start at
    with open("root_nodesIndex.csv", "r") as root_nodes:
        # Find the biggest root node which is not bigger than node_number
        # This will be the root the node_number belongs to
        for node in root_nodes:
            if int(node.split(",")[1]) < node_number:
                root_node = int(node.split(",")[1])

    # Find node in main_data.csv
    with open("main_data.csv", "r") as main_data:
        nodes = main_data.readlines()
        parent = nodes[node_number-1].split(",")
        child_nodes = []
        child_name = []

        # Find the node number of the children of the parent
        for i in range(2, len(parent)):
            child_nodes.append(parent[i])

        # Find the name of each of the node numbers in child_nodes
        for i in range(0, len(child_nodes)) :
            child_name.append(find_node_name(int(child_nodes[i])))

        print (child_name)

def add_node(node_to_add_to, node_name):
    node_to_add_to = node_to_add_to - 1
    node_arr = []
    with open("main_data.csv", "r") as main_data:
        nodes = main_data.readlines()

        for i in range(0, len(nodes)):
            print ("i is " + str(i) + "   and node_to_add_to is " + str(node_to_add_to))
            if i == node_to_add_to:
                print ("equal")
                # Increase all children
                # Add a new child of node number = i to end of current line
                # Append the new child to the array

                # Increment all children
                node = nodes[i].split(",")
                parent_node_name = node[0]
                node_number = node[1]
                children = ""

                # For every child and node number belonging to node
                for i in range(2, len(node)) :
                    # Add one to the number
                    children = children + "," + (str(int(node[i]) + 1))

                # Collate all the values that we just split apart and add a new child at the start with node number i
                line_to_add = parent_node_name + "," + node_number + "," + str(i) + children + "," + "\n"

                node_arr.append(line_to_add)

                node_arr.append(parent_node_name + "," + str(i))
            elif i > node_to_add_to:
                # If i is bigger than node_to_add_to
                # node_name has already been added

                # Define some variables
                node = nodes[i].split(",")
                node_name = node[0]
                children = ""

                # For every child and node number belonging to node
                for i in range(1, len(node)) :
                    # Add one to the number
                    children = children + "," + (str(int(node[i]) + 1))

                # Collate all the values that we just split apart
                line_to_add = node_name + children + "\n"
                
                node_arr.append(line_to_add)
            else:
                node_arr.append(nodes[i])
    
    # Now, node

add_node(1, "myNewNode")
