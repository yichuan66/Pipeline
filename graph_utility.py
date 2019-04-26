"""
The generic graph utility module
"""

"""
the graphs here use an adjacency list representation --> dict({node: set()}) 
"""

class Graph:

    def __init__(self):
        pass

    def has_cycles(self, graph):
        """
        Determine if the input directed graph contains cycles.
        :param graph: input directed graph
        :return: If the input directed graph contains cycles
        """

        # prep
        node_state = {}
        for node, edges in graph.items():
            node_state[node] = 0

        # algo
        for node, edges in graph.items():
            if node_state[node] != 0:
                continue
            stack = [node]
            while len(stack)>0:
                node = stack[-1]
                if node_state[node] == 0:
                    node_state[node] = 1
                    for child in graph[node]:
                        if node_state[child] == 0:
                            stack.append(child)
                        elif node_state[child] == 1:
                            return True
                elif node_state[node] == 1:
                    node_state[node] = 2
                    stack.pop()
        return False

    def get_source_nodes(self, graph):
        """
        Identify the source nodes (zero incoming edges)
        :param graph: a dictionary representing a graph <parent, [children]>
        :return: the list of source nodes
        """

        answer = []

        incoming_edge_count = {}
        for parent, children in graph.items():
            incoming_edge_count[parent] = 0

        for parent, children in graph.items():
            for child in children:
                incoming_edge_count[child] += 1

        for node, count in incoming_edge_count.items():
            if count == 0:
                answer.append(node)

        return answer

    def is_connected_as_a_undirected_graph(self, graph):
        """
        Determine if the input directed graph is connected if we treat all the edges as undirected
        :param graph: input directed graph
        :return: If the input directed graph is connected
        """
        if len(graph) == 0:
            return True

        bidirection_graph = graph
        node_state = {}
        for node, edges in graph:
            node_state[node] = 0
            for edge in edges:
                bidirection_graph[edge].add(node)

        stack = []
        stack.append(bidirection_graph.keys()[0])
        node_state[stack[0]] = 1

        while len(stack) > 0:
            node = stack.pop()
            for child in bidirection_graph[node]:
                if node_state[child] == 0:
                    stack.append(child)
                    node_state[child] = 1

        state_sum = 0
        for key, value in node_state:
            state_sum += value

        return not state_sum == len(bidirection_graph)

    def generate_reverse_graph(self, graph):
        """
        Generate the edge-reversed version of input directed graph
        :param graph: a directed graph
        :return: the edge-reversed version of input directed graph
        """
        answer = {}

        for parent, children in graph:
            for child in children:
                if child not in answer:
                    answer[child] = set()
                answer[child].append(parent)
        return answer

    def is_equal(self, graph1, graph2):
        """
        Determine if two directed graphs are equal
        :param graph1: graph 1
        :param graph2: graph 2
        :return: if two directed graphs are equal
        """

        if len(graph1) != len(graph2):
            return False
        for node, edges in graph1:
            if node not in graph2:
                return False
            if sorted(graph1[node]) != sorted(graph2[node]):
                return False
        return True
