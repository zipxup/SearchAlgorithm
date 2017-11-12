class Node:
    def __init__(self, key, heuristic = 0):
        # self.key is the key of node
        # self.successors are the successors nodes
        # self.weight is the weight of edges
        self.key, self.heuristic = key, heuristic
        self.precessors, self.weight_precessors = [], {} 
        self.successors, self.weight_successors = [], {}

    #return node's key
    def getKey(self):
        return self.key

    #return node's heuristic that estimates the cost of the cheapest path from n to the goal
    def getHeuristic(self):
        return self.heuristic
    
    #return precessors of node
    def getPrecessors(self):
        return self.precessors

    #return successors of node
    def getSuccessors(self):
        return self.successors

    #return weight of precessors:
    def getWeightPrecessors(self):
        return self.weight_precessors

    #return weight of successors:
    def getWeightSuccessors(self):
        return self.weight_successors

    def addPrecessors(self, node, weight):
        # check whether this node exists
        if node.getKey() not in self.weight_precessors:
            self.precessors.append(node)
            self.weight_precessors[node.getKey()] = weight

    def addSuccessors(self, node, weight):
        # check whether this node exists
        if node.getKey() not in self.weight_successors:
            self.successors.append(node)
            self.weight_successors[node.getKey()] = weight

class Graph:
    def __init__(self):
        # key is the key of node
        # value is the instance of Node
        self.nodes = {}

    # add a node in the graph 
    def addNode(self, key, heuristic = 0):
        # check if the key already exists
        if key not in self.nodes:
            node = Node(key, heuristic)
            self.nodes[key] = node            
        else:
            print('key: %s already exists' % key)

    def getNodeHeuristic(self, key):
        if key not in self.nodes:
            print('key: %s not exist' % key)
        else:
            node = self.nodes[key]
            return node.getHeuristic()

    # connect two nodes with weight
    def connectNodes(self, sourceKey, destKey, weight):
        # check if those keys exist in the graph
        if sourceKey not in self.nodes or destKey not in self.nodes:
            print('key does not exist')
            return

        # check whether they share same key
        if sourceKey == destKey:
            print('same keys')
            return
        
        # check weight, only accept positive numbers
        if weight <= 0:
            print('weight should be positive')
            return

        self.nodes[sourceKey].addSuccessors(self.nodes[destKey], weight)
        self.nodes[destKey].addPrecessors(self.nodes[sourceKey], weight)

    #return weight of edge
    def getEdgeWeight(self, sourceKey, successor):
        if sourceKey not in self.nodes or successor not in self.nodes:
            print('key does not exist')
            return

        # check whether they share same key
        if sourceKey == successor:
            print('same keys')
            return
        
        weight_successors = self.nodes[sourceKey].getWeightSuccessors()
        # check if successor is in successors list
        if successor not in weight_successors:
            print('successor not exist')
            return

        return weight_successors[successor]

    # return keys of all precessors of a node
    def getPrecessors(self, key):
        if key not in self.nodes:
            print('key does not exist')
            return

        precessors = self.nodes[key].getPrecessors()
        key_precessors = [node.getKey() for node in precessors]
        return sorted(key_precessors)

    # return keys of all successors of a node
    def getSuccessors(self, key):
        if key not in self.nodes:
            print('key does not exist')
            return

        successors = self.nodes[key].getSuccessors()   
        key_successors = [node.getKey() for node in successors]     
        return sorted(key_successors)

    # return all nodes
    def getNodes(self):
        return self.nodes
