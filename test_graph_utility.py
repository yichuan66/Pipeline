from unittest import TestCase
from graph_utility import *

class TestGraph(TestCase):
    def test_has_cycles(self):
        def new_test_case(test_case_name, graph, expected_has_cycles):
            return {
                "test_case_name" : test_case_name,
                "graph" : graph,
                "expected_has_cycles" : expected_has_cycles
            }

        def test_logic(test, test_case):
            g = Graph()
            test.assertEqual(g.has_cycles(graph=test_case["graph"]), test_case["expected_has_cycles"])

        test_cases = [
            new_test_case("empty graph", {}, False),
            new_test_case("single node graph", {1: set()}, False),
            new_test_case("self loop node", {1: set([1])}, True),
            new_test_case("singly linked list", {1: set([2]), 2: set([3]), 3: set([])}, False),
            new_test_case("no cycle graph 1", {1: set([2, 3]), 2: set(), 3: set([])}, False),
            new_test_case("no cycle graph 2", {1: set(), 2: set([1]), 3: set([1])}, False),
            new_test_case("no cycle graph 3", {1: set([2, 3]), 2: set([4]), 3: set([4]), 4: set()}, False),
            new_test_case("cycle graph 1", {1: set([2]), 2: set([3]), 3: [1]}, True),
            new_test_case("cycle graph 2", {1: set([2]), 2: set([1])}, True),
            new_test_case("cycle graph 3", {1: set([2, 3]), 2: set([3, 4]), 3: set([4]), 4: set()}, False),
            new_test_case("cycle graph 4", {1: set([2, 3]), 2: set([4]), 3: set([3, 4]), 4: set()}, True)
        ]

        for tc in test_cases:
            test_logic(self, tc)

    def test_get_source_nodes(self):
        self.fail()

    def is_connected_as_a_undirected_graph(self):
        self.fail()

    def test_generate_reverse_graph(self):
        self.fail()

    def test_is_same_graph(self):
        self.fail()
