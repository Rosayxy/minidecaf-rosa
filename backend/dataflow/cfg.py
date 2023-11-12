from backend.dataflow.basicblock import BasicBlock

"""
CFG: Control Flow Graph

nodes: sequence of basicblock
edges: sequence of edge(u,v), which represents after block u is executed, block v may be executed
links: links[u][0] represent the Prev of u, links[u][1] represent the Succ of u,
"""


class CFG:
    def __init__(self, nodes: list[BasicBlock], edges: list[(int, int)]) -> None:
        self.nodes = nodes
        self.edges = edges
        self.reachable_nodes=set()
        self.links = []

        for i in range(len(nodes)):
            self.links.append((set(), set()))

        for (u, v) in edges:
            self.links[u][1].add(v)
            self.links[v][0].add(u)

        #go to the head
        head=0
        for (u,v) in edges:
            if self.getInDegree(u)==0:
                head=u
                break
        self.reachable_nodes.add(self.getBlock(head))
        #queue to help bfs
        que = []
        que.append(head)
        while que.__len__():
            cur=que.pop(0)
            for i in self.links[cur][1]:
                if self.getBlock(i) not in self.reachable_nodes:
                    self.reachable_nodes.add(self.getBlock(i))
                    que.append(i)                    
        """
        You can start from basic block 0 and do a DFS traversal of the CFG
        to find all the reachable basic blocks.
        """

    def getBlock(self, id):
        return self.nodes[id]

    def getPrev(self, id):
        return self.links[id][0]

    def getSucc(self, id):
        return self.links[id][1]

    def getInDegree(self, id):
        return len(self.links[id][0])

    def getOutDegree(self, id):
        return len(self.links[id][1])

    def iterator(self):
        list_iter=[]
        for i in self.nodes:
            if self.reachable_nodes.__contains__(i):
                list_iter.append(i)
        return iter(list_iter)
