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

    # Search this node in mainData.csv
    with open("mainData.csv", "r") as mainData:
        nodes = mainData.readlines()
        return nodes[nodeNumber].split(",")[0]

print(findNodeName(5))