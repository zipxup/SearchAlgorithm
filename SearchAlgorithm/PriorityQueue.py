import heapq

class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0

    def insert(self, item, priority):
        heapq.heappush(self.__queue, (priority, self.__index, item))
        self.__index = self.__index + 1

    # remove the one with lowest priority
    def remove(self):
        return heapq.heappop(self.__queue)[-1]

    def is_empty(self):
        return len(self.__queue) == 0

    


#queue = PriorityQueue()
#queue.insert('e', 9)
#queue.insert('a', 2)
#queue.insert('h', 13)
#queue.insert('e', 5)
#queue.insert('c', 11)
#print(queue.remove())
