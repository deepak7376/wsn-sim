# tests/test_network.py
import unittest
from wsn_sim.node import Node
from wsn_sim.network import Network
import random

class TestWirelessSensorNetwork(unittest.TestCase):

    def setUp(self):
        self.net = Network()
        self.base_station = Node(0, (50, 50), role='base_station', protocol='AODV')
        self.net.add_node(self.base_station)

        for i in range(1, 5):
            node = Node(i, (random.randint(0, 100), random.randint(0, 100)), protocol='AODV')
            self.net.add_node(node)

        self.net.add_link(0, 1)
        self.net.add_link(1, 2)
        self.net.add_link(2, 3)
        self.net.add_link(3, 4)

    def test_node_creation(self):
        node = Node(5, (10, 10), protocol='AODV')
        self.assertEqual(node.node_id, 5)
        self.assertEqual(node.position, (10, 10))
        self.assertEqual(node.role, 'sensor')
        self.assertEqual(node.energy, 100)
        self.assertEqual(node.protocol, 'AODV')

    def test_add_node_to_network(self):
        node = Node(6, (20, 20), protocol='AODV')
        self.net.add_node(node)
        self.assertIn(node, self.net.nodes)

    def test_add_link(self):
        self.net.add_link(0, 2)
        self.assertTrue(self.net.graph.has_edge(0, 2))

    def test_node_transmit(self):
        node1 = self.net.node_mapping[1]
        node2 = self.net.node_mapping[2]
        initial_energy = node1.energy
        data = {'content': 'Hello', 'destination': node2}
        node1.transmit(data['content'], node2)
        self.assertLess(node1.energy, initial_energy)

    def test_run_simulation(self):
        self.net.run_simulation(steps=2, protocol='AODV')
        for node in self.net.nodes:
            self.assertIsNotNone(node.energy)

class TestDSRProtocol(unittest.TestCase):

    def setUp(self):
        self.net = Network()
        self.base_station = Node(0, (50, 50), role='base_station', protocol='DSR')
        self.net.add_node(self.base_station)

        for i in range(1, 5):
            node = Node(i, (random.randint(0, 100), random.randint(0, 100)), protocol='DSR')
            self.net.add_node(node)

        self.net.add_link(0, 1)
        self.net.add_link(1, 2)
        self.net.add_link(2, 3)
        self.net.add_link(3, 4)

    def test_node_creation(self):
        node = Node(5, (10, 10), protocol='DSR')
        self.assertEqual(node.node_id, 5)
        self.assertEqual(node.position, (10, 10))
        self.assertEqual(node.role, 'sensor')
        self.assertEqual(node.energy, 100)
        self.assertEqual(node.protocol, 'DSR')

    def test_add_node_to_network(self):
        node = Node(6, (20, 20), protocol='DSR')
        self.net.add_node(node)
        self.assertIn(node, self.net.nodes)

    def test_add_link(self):
        self.net.add_link(0, 2)
        self.assertTrue(self.net.graph.has_edge(0, 2))

    def test_node_transmit(self):
        node1 = self.net.node_mapping[1]
        node2 = self.net.node_mapping[2]
        initial_energy = node1.energy
        data = {'content': 'Hello', 'destination': node2}
        node1.transmit(data['content'], node2)
        self.assertLess(node1.energy, initial_energy)

    def test_run_simulation(self):
        self.net.run_simulation(steps=2, protocol='DSR')
        for node in self.net.nodes:
            self.assertIsNotNone(node.energy)

if __name__ == '__main__':
    unittest.main()
