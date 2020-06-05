class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        to_flip = 0 # this tracks how many edges we need to flip.

        # we construct a set here so we get membership checks in O(1).
        # note that the conversion into a tuple (x,y) is needed because the original input uses lists, which are unhashable.
        original_edges = set([(x,y) for (x,y) in connections])


        edge_dict = defaultdict(list) # set up our edges for graph traversal.
        for (i,j) in connections:
            edge_dict[i].append(j)
            edge_dict[j].append(i)
            
        visited = set() # make sure we don't go in a loop.
        stack = [0] # we'll do a DFS and start at node 0.
        while stack:
            node = stack.pop()
            visited.add(node)
            for next_node in edge_dict[node]: # for each node that the current node is connected to,
                if next_node not in visited:  # check that we haven't visited it before.
                    stack.append(next_node)   # add it to the stack so we can explore it next.

                    # if this edge exists in the set of original edges, we need to flip it.
                    if (node, next_node) in original_edges:
                        to_flip += 1
        return to_flip
