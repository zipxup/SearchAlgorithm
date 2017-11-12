from WeightedGraph import *
import os

class ParseFile(object):
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__graphlist = list()
        #self.algo = ' '
        self.start = ' '
        self.goal = ' '
        self.pathNum = 0
        self.pathList = list()
        self.nodeNum = 0
        self.nodeList = list()

    def checkFile(self):
        file_exist = os.path.isfile(self.__fileName)
        if file_exist:
            with open(self.__fileName, mode = 'r') as inputFile:
                allRowList = inputFile.readlines()
                if allRowList:
                    for line in allRowList:
                        line = line.strip('\n')
                        self.__graphlist.append(line)
                else:
                    print('it is an empty file')
                    return False
        else:
             print('File doesn\'t exist')
             return False  
        return True          
    def getGraphList(self):
        return self.__graphlist

    #def __getSearchAlgorithm__(self):
    #    return self.__graphlist[0]

    def __getStart__(self):
        return self.__graphlist[0]

    def __getGoal__(self):
        return self.__graphlist[1]

    def __getNodeNum__(self):
        return int(self.__graphlist[2])

    def __getNodeList__(self):
        start = 3
        stop = start + self.nodeNum
        for index in range(start, stop):
            node = self.__graphlist[index].split()
            self.nodeList.append(node)

    def __getPathNum__(self):
        return int(self.__graphlist[3 + self.nodeNum])

    def __getPathList__(self):
        start = 3 + self.nodeNum + 1
        stop = start + self.pathNum
        for index in range(start, stop):
            path = self.__graphlist[index].split()
            self.pathList.append(path)

    def parse(self):
        #self.algo = self.__getSearchAlgorithm__()
        self.start = self.__getStart__()
        self.goal = self.__getGoal__()
        self.nodeNum = self.__getNodeNum__()
        self.__getNodeList__()
        self.pathNum = self.__getPathNum__()
        self.__getPathList__()        


class LoadGraph(object):
    def __init__(self, pathList, nodeList):
        self.__pathList = pathList
        self.__nodeList = nodeList
        self.graph = Graph()

    def createGraph(self):
        self.__loadNodeList__()
        self.__loadPathList__()    

    def __loadNodeList__(self):
        for node in self.__nodeList:
            self.graph.addNode(node[0], float(node[1]))

    def __loadPathList__(self):
        for path in self.__pathList:
            self.graph.connectNodes(path[0], path[1], float(path[2]))

  
    