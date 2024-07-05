# wsn_sim/cli.py
import click
from wsn_sim.network import Network
from wsn_sim.node import Node
import random
import configparser

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

@click.command()
@click.option('--config', type=click.Path(exists=True), help='Path to the configuration file')
@click.option('--protocol', type=click.Choice(['AODV', 'DSR']), help='Choose the routing protocol (AODV/DSR)')
@click.option('--steps', type=int, help='Number of simulation steps')
@click.option('--nodes', type=int, help='Number of nodes in the network')
@click.option('--links', type=int, help='Number of random links between nodes')
def run_simulation(config, protocol, steps, nodes, links):
    if config:
        cfg = read_config(config)
        protocol = cfg.get('simulation', 'protocol', fallback='AODV')
        steps = cfg.getint('simulation', 'steps', fallback=10)
        nodes = cfg.getint('simulation', 'nodes', fallback=20)
        links = cfg.getint('simulation', 'links', fallback=30)
    else:
        protocol = protocol or 'AODV'
        steps = steps or 10
        nodes = nodes or 20
        links = links or 30

    net = Network()
    base_station = Node(0, (50, 50), role='base_station', protocol=protocol)
    net.add_node(base_station)

    for i in range(1, nodes):
        node = Node(i, (random.randint(0, 100), random.randint(0, 100)), protocol=protocol)
        net.add_node(node)

    for _ in range(links):
        node1 = random.choice(net.nodes)
        node2 = random.choice(net.nodes)
        if node1 != node2:
            net.add_link(node1.node_id, node2.node_id)

    net.run_simulation(steps=steps, protocol=protocol)
    net.visualize()

if __name__ == '__main__':
    run_simulation()
