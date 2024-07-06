# WSN-Simulator (WSN-Sim)

**WSN-Sim** is a Python-based Wireless Sensor Network (WSN) simulator supporting AODV and DSR protocols.

## Installation

To install the package, run the following command:

```bash
pip install wsn-sim
```

## Usage

You can use the simulator by specifying options directly via the command line:

```bash
wsn-sim --protocol AODV --steps 10 --nodes 20 --links 30 --topology random
```

Alternatively, you can define these parameters in a `.cfg` file and provide the file path:

```ini
# config.cfg

[simulation]
protocol = AODV
steps = 10
nodes = 20
links = 30
topology = random
```

Then run:

```bash
wsn-sim --config config.cfg
```

## Options

- `--config`: Path to the configuration file
- `--protocol`: Choose the routing protocol (AODV/DSR)
- `--steps`: Number of simulation steps
- `--nodes`: Number of nodes in the network
- `--links`: Number of random links between nodes
- `--topology`: Network topology (grid/random/cluster)

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Example

Here is an example of how to use the simulator:

1. Define your simulation parameters in a `.cfg` file:

    ```ini
    # simulation_config.cfg
    [simulation]
    protocol = DSR
    steps = 15
    nodes = 25
    links = 50
    topology = random
    ```

2. Run the simulation using the configuration file:

    ```bash
    wsn-sim --config simulation_config.cfg
    ```

3. Alternatively, run the simulation with parameters directly from the command line:

    ```bash
    wsn-sim --protocol DSR --steps 15 --nodes 25 --links 50 --topology cluster
    ```

## License

This project is licensed under the MIT License.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements, including bug fixes, new features, and documentation enhancements.

