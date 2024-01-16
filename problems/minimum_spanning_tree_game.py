import sys
input = sys.stdin.readline

# Class to represent a graph 
class Graph: 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 

    # Function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 

    def removeEdge(self, i):
        self.graph.pop(i)

    # A utility function to find set of an element i 
    # (truly uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 

            # Reassignment of node's parent 
            # to root node as 
            # path compression requires 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 

        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 

        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else: 
            parent[y] = x 
            rank[x] += 1

    # The main function to construct MST 
    # using Kruskal's algorithm 
    def KruskalMST(self, step): 

        # This will store the resultant MST 
        result = [] 

        # An index variable, used for sorted edges 
        i = 0

        # An index variable, used for result[] 
        e = 0

        # Sort all the edges in 
        # non-decreasing order of their 
        # weight 
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 

        parent = [] 
        rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        # Number of edges to be taken is less than to V-1 
        while e < self.V - 1 and i < len(self.graph): 

            # Pick the smallest edge and increment 
            # the index for next iteration 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 

            # If including this edge doesn't 
            # cause cycle, then include it in result 
            # and increment the index of result 
            # for next edge 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
            # Else discard the edge 

        minimumCost = 0
        # print("Edges in the constructed MST") 
        if (e == self.V - 1):
            minW = sys.maxsize
            for u, v, weight in result:
                minimumCost += weight
                minW = min(minW, weight)
            # print(weight-step-1)
            self.graph.pop(minW-step-1)
            # print("%d -- %d == %d" % (u, v, weight)) 
        # print("Minimum Spanning Tree", minimumCost)
        return minimumCost

# Driver code 
if __name__ == '__main__': 
    N, M, K = [int(i) for i in input().split()]
    ans = [0 for i in range(K)]
    g = Graph(N)
    for i in range(M):
        tmp = [int(j)-1 for j in input().split()]
        g.addEdge(tmp[0], tmp[1], i+1)
    
    for i in range(K):
        ans[i] = g.KruskalMST(i)
        if (ans[i] == 0):
            break
    
    print(*ans)
