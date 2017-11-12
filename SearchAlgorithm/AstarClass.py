from PriorityDict import *
from WeightedGraph import *

class AstarClass(object):
    def __init__(self, graph):
        self.__graph = graph
        # open stores node's f_value
        self.open = PriorityDict()
        # closed stores visited node's g_value, a.k.a cost
        self.closed = dict()

    def A_star_search(self, start, goal):
        if start not in self.__graph.getNodes():
            print('start node : %s not exist' % start)
            return
        if goal not in self.__graph.getNodes():
            print('goal node : %s not exist' % goal)
            return
        
        # f_value = h_value + g_value
        # h_value: heuristic value
        # g_value: cost from start node to the current node
        h_value = self.__graph.getNodeHeuristic(start)
        self.open.set_item(start, h_value)
        while self.open:
            current_node, current_f_value = self.open.pop_smallest()
            self.closed[current_node] = current_f_value - self.__graph.getNodeHeuristic(current_node)
            
            if current_node == goal:                
                return self.show_path(start, goal)

            successors = self.__graph.getSuccessors(current_node)
            #check if current node has successors
            if successors:                
                for successor in successors:
                    self.push_successor(current_node, successor)
                    self.open.update()


    def push_successor(self, current, successor):
        # calculate current f_value for successor
        cumulative_cost = self.__graph.getEdgeWeight(current, successor) + self.closed[current]
        cumulative_f_value = self.__graph.getNodeHeuristic(successor) + cumulative_cost

        if successor not in self.open and successor not in self.closed:            
            self.open.set_item(successor, cumulative_f_value)

        # if successor is already in open dictionary,
        # but its value is larger than the new path value
        # then update it
        elif successor in self.open and successor not in self.closed:
            if self.open[successor] > cumulative_f_value:
                self.open.set_item(successor, new_cost)

        # if successor is already in closed dictionary,
        # but its value is larger than the new path value
        # then delete it and re-add it to the open dictionary
        elif successor not in self.open and successor in self.closed:
            if self.closed[successor] > cumulative_cost:
                del self.closed[successor]
                self.open.set_item(successor, cumulative_f_value)


    def check_precessor(self, precessor, current):
        if precessor in self.closed:
            if self.closed[current] == self.closed[precessor] + self.__graph.getEdgeWeight(precessor, current):
                return True
        return False 

    def show_path(self, start, goal):
        path = dict()
        total_cost = self.closed[goal]
        path[goal] = total_cost - self.closed[goal]

        current = goal
        while current != start:
            precessors = self.__graph.getPrecessors(current)
            if precessors:
                for node in precessors:
                    exist_flag = self.check_precessor(node, current)
                    if exist_flag:
                        path[node] = total_cost - self.closed[node]
                        current = node
                        break
            else:
                break

        return self.print_path(path)
        

    def print_path(self, path):
        # sort by value in decreased order
        # after sorted, dictionary becomes list
        path = sorted(path.items(), key = lambda x : x[1], reverse = True)
        result = "A* \n"
        for node in path:
            #print(node[0] + ' => %d' %node[1])
            result += node[0] + " => " + str(node[1]) + "\n"
        return result