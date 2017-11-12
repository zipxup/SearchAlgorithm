import heapq

class PriorityDict(dict):
    # dictionary can be used as a prioriy queue

    # keys : items to be put into the queue
    # values: their respective priorityes
    # The advantage over a standard heapq-based priority queue
    # is that priorities of items can be efficiently updated

    def __init__(self, *args, **kwargs):
        super(PriorityDict, self).__init__(*args, **kwargs)
        self.rebuild_heap()
        
    def rebuild_heap(self):
        self.__heap = [(v, k) for k, v in self.items()]
        heapq.heapify(self.__heap)

    #return the item with the lowest priority
    def smallest(self):
        heap = self.__heap
        v, k = heap[0]
        while k not in self or self[k] != v:
            heapq.heappop(heap)
            v, k = heap[0]
        return k

    #return the item with the lowest priority and remove it
    def pop_smallest(self):
        heap = self.__heap
        v, k = heap[0]
        while k not in self or self[k] != v:
            heapq.heappop(heap)
            v, k = heap[0]
        del self[k]
        return k, v

    def set_item(self, key, value):
        super(PriorityDict, self).__setitem__(key, value)

        if len(self.__heap) < 2 * len(self):
            heapq.heappush(self.__heap, (value, key))
        else:
            # when the heap grows larger than 2 * len(self),
            # rebuild it from scratch to avoid wasting too much memory
            self.rebuild_heap()

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value
            return value
        return self[key]

    def update(self, *args, **kwargs):
        super(PriorityDict, self).update(*args, **kwargs)
        self.rebuild_heap()

    def get_heap(self):
        return self.__heap

#priority = PriorityDict()
#priority.set_item('a', 9)
#priority.set_item('b', 5)
#priority.set_item('c', 3)
#priority.set_item('d', 1)
#priority.set_item('e', 13)
#priority.set_item('a', 2)

#print(priority.pop_smallest())
#print(priority)
#print(priority['a'])
#priority['a'] = 3
#print(priority['a'])
#print(priority)
#print(priority.get_heap())
#priority.update()
#print(priority.get_heap())
