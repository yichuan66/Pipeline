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
            new_test_case("single node graph", {1: []}, False),
            new_test_case("self loop node", {1: [1]}, True),
            new_test_case("singly linked list", {1: [2], 2: [3], 3: []}, False),
            new_test_case("no cycle graph 1", {1: [2, 3], 2: [], 3: []}, False),
            new_test_case("no cycle graph 2", {1: [], 2: [1], 3: [1]}, False),
            new_test_case("no cycle graph 3", {1: [2, 3], 2: [4], 3: [4], 4: []}, False),
            new_test_case("cycle graph 1", {1: [2], 2: [3], 3: [1]}, True),
            new_test_case("cycle graph 2", {1: [2], 2: [1]}, True),
            new_test_case("cycle graph 3", {1: [2, 3], 2: [3, 4], 3: [4], 4: []}, False),
            new_test_case("cycle graph 4", {1: [2, 3], 2: [4], 3: [3, 4], 4: []}, True)
        ]

        for tc in test_cases:
            test_logic(self, tc)

    def test_get_source_nodes(self):
        self.fail()

    def test_is_connected(self):
        self.fail()
