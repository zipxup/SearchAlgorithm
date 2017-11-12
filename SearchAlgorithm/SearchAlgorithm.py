from DFSClass import *
from BFSClass import *
from UniformCostSearch import *
from AstarClass import *
from LoadGraphFile import *


parseFile = ParseFile('input.txt')
fileExist = parseFile.checkFile()

if fileExist:
    parseFile.parse()
    loadGraph = LoadGraph(parseFile.pathList, parseFile.nodeList)
    loadGraph.createGraph()
    if parseFile.algo == 'BFS':
        bfs = BFSclass(loadGraph.graph)
        bfs.bfs_shortest_path(parseFile.start, parseFile.goal)
    elif parseFile.algo == 'DFS':
        dfs = DFSclass(loadGraph.graph)
        dfs.dfs_first_path(parseFile.start, parseFile.goal)
    elif parseFile.algo == 'UCS':
        ucs = UCSclass(loadGraph.graph)
        ucs.uniform_cost_search(parseFile.start, parseFile.goal)
    elif parseFile.algo == 'A*':
        astar = AstarClass(loadGraph.graph)
        astar.A_star_search(parseFile.start, parseFile.goal)


