from WeightedGraph import *

# class for Depth-First-Search
class DFSclass(object):
    def __init__(self, graph):
        self.__graph = graph
        self.__visited = list()        

    # iteration part
    def dfs_iteration(self, start):
        stack = [start]
        while stack:
            current = stack.pop()
            if current not in self.__visited:
                self.__visited.append(current)
                successors = self.__graph.getSuccessors(vertex)
                if successors: 
                    unvisited = list(set(successors) - set(self.__visited))
                    unvisited.sort()
                    stack.extend(unvisited)
        return self.__visited

    # show all paths from start to goal
    def dfs_iteration_paths(self, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            successors = self.__graph.getSuccessors(vertex)
            if successors:          
                for next in successors:
                    if next not in path:
                        if next == goal:
                            yield path + [next]
                        else:
                            stack.append((next, path + [next]))

    #recursion part
    def dfs_recursion(self, start):
        self.__visited.append(start)
        successors = self.__graph.getSuccessors(start)
        if successors: 
            for next in successors:
                if next not in self.__visited:
                    self.dfs_recursion(next)
        return self.__visited

    # show all paths from start to goal
    def dfs_recursion_paths(self, start, goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path

        successors = self.__graph.getSuccessors(start)
        if successors: 
            for next in successors:
                if next not in path:
                    yield from self.dfs_recursion_paths(next, goal, path+[next])

    def dfs_first_path(self, start, goal):
        try:
            path = next(self.dfs_recursion_paths(start, goal))
            return self.print_path(path)
        except StopIteration:
            return None

    def print_path(self, path):
         result = "DFS \n"
         cost = len(path) - 1
         for node in path:
            #print(node + " => %d" %cost)
            result += node + " => " + str(cost) + "\n"
            cost = cost - 1
         return result

