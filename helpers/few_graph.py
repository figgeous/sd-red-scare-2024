import sys
# from this implementation: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {} # new, empty, dictionary
        for node in nodes: 
            graph[node] = {} # each node is a key, new empty dictionary as value
        
        graph.update(init_graph) #dictionary function in standard python -> here I need to pass my values
        
        for node, edges in graph.items():
            # Ensure the graph is symmetrical by checking if the reverse path exists
            for adjacent_node, value in edges.items():
            #   if for adjecent node, we don't have the node we just checked, then create it
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self): #return list of nodes in the graph
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]