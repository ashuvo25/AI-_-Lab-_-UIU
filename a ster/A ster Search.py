
#  /*******************বিসমিল্লাহির রাহমানির রাহিম **********************/
# /* 
#         author : md asaduzzaman shuvo
#            date: 25-02-2024  01:22:01
# */ 

adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('D', 2), ('G', 3)],
    'D': [('G', 2), ('A', 2)],
    'G': [('C', 4)],
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0,
}

class Node:
    def __init__(self, nodename, parent, g, h):
        self.nodename = nodename
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

class ManualPriorityQueue:
    def __init__(self):
        self.queue = []
    def push(self, item):
        self.queue.append(item)
        self.queue.sort(key=lambda x: x.f)
    def pop(self):
        return self.queue.pop(0)
    def empty(self):
        return len(self.queue) == 0


pqueue = ManualPriorityQueue()
start_node = Node('S', None, 0, H['S'])
pqueue.push(start_node)
NOb = None #corrent node
while not pqueue.empty():
    NOb = pqueue.pop()
    if NOb.nodename == 'G':
        break
    for neighbor, edge_cost in adjacency_list[NOb.nodename]:
        new_node = Node(neighbor, NOb, NOb.g + edge_cost, H[neighbor])
        pqueue.push(new_node)

path = []
cost = NOb.g
while NOb is not None:
    
    path.insert(0, NOb.nodename)
    NOb = NOb.parent
    # print(NOb.parent)

print("Path:", path)
print("Cost:", cost)
