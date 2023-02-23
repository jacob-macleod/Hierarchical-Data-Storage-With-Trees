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
    with open("root_nodes_index.csv", "r") as root_nodes:
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

""" Look at every number in the csv file (node index number and children indexes)
If there is a number smaller than node_to_add_to, do nothing
If there is a number bigger than node_to_add_to, increment it
When you reach the node_to_add_to line, add the item"""
def add_node(node_to_add_to, node_name) :
    file = []

    # Look at every line in the file
    with open("main_data.csv", "r") as main_data:
        for line in main_data:
            line_arr = line.split(",")
            print (line_arr)
            # Look at the node number
            node_number = line_arr[1]
            # if node_number > node_to_add_to, increment it
            if int(node_number) > node_to_add_to:
                node_number = str(int(node_number) + 1)

            # Select all the children of the element
            children = ""
            for child_number in range(2, len(line_arr)) :
                # Add one to the number if the number > node_number
                if int(line_arr[child_number]) > node_to_add_to:
                    children = children + "," + (str(int(line_arr[child_number]) + 1))
                else :
                    children = children + "," + str(int(line_arr[child_number]))
            
            # If the line to add the item to has not been reached
            if int(node_number) != node_to_add_to :
                # Save the item
                line_to_add = line_arr[0] + "," + node_number + children
                file.append(line_to_add)
            else :
                line_to_add = line_arr[0] + "," + node_number.replace("\n", "") + "," + str(node_to_add_to + 1) + children
                file.append(line_to_add)
                # Add the element
                file.append(node_name + "," + str(node_to_add_to + 1))
    
    # Save the contents of file back into the original document
    with open("main_data.csv", "w") as main_data:
        for line_number in range(0, len(file)):
            main_data.write(file[line_number] + "\n")
# Get a list of the root nodes
def update_root_nodes() :
    children = []
    root_nodes = []

    # For every line in the file
    with open("main_data.csv", "r") as main_data:
        for line in main_data:
            line_arr = line.split(",")
            # Save the children to the array if they have not already been saved
            for child_number in range(2, len(line_arr)) :
                # Look through children
                child_used = False
                for child in range(0, len(children)) :
                    if children[child] == line_arr[child_number].replace("\n", ""):
                        child_used = True

                # If the child is not already saved
                children.append(line_arr[child_number].replace("\n", ""))

    # Now, look through the file again
    # If the node_number is not in children, add it to root_nodes
    with open("main_data.csv", "r") as main_data:
        for line in main_data:
            line_arr = line.split(",")
            node_number = line_arr[1].replace("\n", "")
            node_number_used = False

            # See if the node_number is in children
            for child in range(0, len(children)) :
                if node_number == children[child]:
                    node_number_used = True

            # If the node is not in children
            if node_number_used == False:
                root_nodes.append(line_arr[0] + "," + node_number)

    # Now you have a list of root nodes, save it to root_nodes_index
    with open("root_nodes_index.csv", "w") as root_nodes_index:
        for node in range(0, len(root_nodes)) :
            root_nodes_index.write(root_nodes[node] + "\n")


update_root_nodes()


