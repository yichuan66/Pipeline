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
            # new_test_case("empty graph", {}, False),
            new_test_case("single node graph", {1 : []}, False)
        ]

        for tc in test_cases:
            test_logic(self, tc)

    def test_get_source_nodes(self):
        self.fail()

    def test_is_connected(self):
        self.fail()
