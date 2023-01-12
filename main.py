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
        return nodes[nodeNumber].split(",")[0]

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
        parent = nodes[nodeNumber].split(",")

        # Find the children of the parent
        for i in range(2, len(parent)):
            print (parent[i])

print(listChildrenOfNode(2))