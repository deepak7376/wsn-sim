# wsn_simulator/cli.py

import click
import configparser
from wsn_sim.network import Network
from wsn_sim.node import Node

def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    simulation_config = {
        'protocol': config.get('simulation', 'protocol'),
        'steps': config.getint('simulation', 'steps'),
        'nodes': config.getint('simulation', 'nodes'),
        'links': config.getint('simulation', 'links'),
        'topology': config.get('simulation', 'topology')
    }
    return simulation_config

@click.command()
@click.option('--config', type=click.Path(), help='Path to the configuration file')
@click.option('--protocol', type=str, default='AODV', help='Routing protocol (AODV/DSR)')
@click.option('--steps', type=int, default=10, help='Number of simulation steps')
@click.option('--nodes', type=int, default=20, help='Number of nodes in the network')
@click.option('--links', type=int, default=30, help='Number of random links between nodes')
@click.option('--topology', type=str, default='cluster', help='Network topology (grid/random/cluster)')
@click.option('--output', type=str, default='graph_visualization.png', help='Output filename for the graph image')
@click.option('--gui', is_flag=True, help='Launch the GUI for the simulation')
def run_simulation(config, protocol, steps, nodes, links, topology, output, gui=True):
    if True:
        Network().create_gui()
        return

    if config:
        config_values = read_config(config)
        protocol = config_values['protocol']
        steps = config_values['steps']
        nodes = config_values['nodes']
        links = config_values['links']
        topology = config_values['topology']

    net = Network()
    net.generate_topology(topology, nodes, links)
    base_station = Node(0, (50, 50), role='base_station')
    net.add_node(base_station)

    if protocol.upper() == 'AODV':
        net.run_aodv_simulation(steps)
    elif protocol.upper() == 'DSR':
        net.run_dsr_simulation(steps)

    net.visualize(filename=output)  # Save the graph to the specified file

if __name__ == '__main__':
    run_simulation()
