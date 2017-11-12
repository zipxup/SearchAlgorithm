from WeightedGraph import *

class BFSclass(object):
    def __init__(self, graph):
        self.__graph = graph
        self.__visited = list()

    def bfs(self, start):
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in self.__visited:
                self.__visited.append(vertex)
                successors = self.__graph.getSuccessors(vertex)
                if successors: 
                    unvisited = list(set(successors) - set(self.__visited))
                    unvisited.sort()
                    queue.extend(unvisited)
        return self.__visited


    def bfs_paths(self, start, goal):
        queue = [(start, [start])]
        while queue:
            # (vertex, path) = queue.pop(0) is slower than popleft() 
            (vertex, path) = queue.pop(0)
            successors = self.__graph.getSuccessors(vertex)
            if successors:
                for next in successors:
                    if next not in path:
                        if next == goal:
                            yield path + [next]
                        else:
                            queue.append((next, path + [next]))


    def bfs_shortest_path(self, start, goal):
        try:            
            path = next(self.bfs_paths(start, goal))
            return self.print_path(path)
        except StopIteration:
            return None

    def print_path(self, path):
        cost = len(path) - 1
        result = "BFS \n"
        for node in path:
            #print(node + " => %d" %cost)
            result += node + " => " + str(cost) + "\n"
            cost = cost - 1
        return result
            