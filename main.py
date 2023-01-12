# Find a node's name from it's number
def findNodeName(nodeNumber) :
    rootNode = 1
    # Decide which root to start at
    with open("rootNodesIndex.csv", "r") as rootNodes:
        # Find the biggest root node which is not bigger than nodeNumber
        # This will be the root the nodeNumber belongs to
        for node in rootNodes:
            if int(node.split(",")[1]) < nodeNumber:
                rootNode = int(node.split(",")[1])

    # Find node in mainData.csv
    with open("mainData.csv", "r") as mainData:
        nodes = mainData.readlines()
        return nodes[nodeNumber-1].split(",")[0]

def listChildrenOfNode(nodeNumber) :
    rootNode = 1
    # Decide which root to start at
    with open("rootNodesIndex.csv", "r") as rootNodes:
        # Find the biggest root node which is not bigger than nodeNumber
        # This will be the root the nodeNumber belongs to
        for node in rootNodes:
            if int(node.split(",")[1]) < nodeNumber:
                rootNode = int(node.split(",")[1])

    # Find node in mainData.csv
    with open("mainData.csv", "r") as mainData:
        nodes = mainData.readlines()
        parent = nodes[nodeNumber-1].split(",")
        childNodes = []
        childNames = []

        # Find the node number of the children of the parent
        for i in range(2, len(parent)):
            childNodes.append(parent[i])

        # Find the name of each of the node numbers in childNodes
        for i in range(0, len(childNodes)) :
            childNames.append(findNodeName(int(childNodes[i])))

        print (childNames)