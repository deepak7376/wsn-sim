import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .network import Network
from .node import Node

class NetworkGUI:
    def __init__(self):
        self.network = Network()
        self.setup_gui()

    def setup_gui(self):
        root = tk.Tk()
        root.title("WSN Simulation GUI")

        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        def run_simulation_gui():
            num_nodes = int(nodes_entry.get())
            num_links = int(links_entry.get())
            topology = topology_var.get()
            steps = int(steps_entry.get())
            output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            if not output_file:
                messagebox.showerror("Error", "No output file selected.")
                return

            self.network.generate_topology(topology, num_nodes, num_links)
            base_station = Node(0, (50, 50), role='base_station')
            self.network.add_node(base_station)

            def update_gui():
                self.network.update_gui(self.ax, self.canvas)
                if self.network.data_transmissions:
                    log_text.set('\n'.join(self.network.data_transmissions))

            if protocol_var.get().upper() == 'AODV':
                self.network.run_aodv_simulation(steps, update_gui)
            elif protocol_var.get().upper() == 'DSR':
                self.network.run_dsr_simulation(steps, update_gui)

            self.network.visualize(filename=output_file)
            messagebox.showinfo("Info", "Simulation completed and graph saved.")

        tk.Label(root, text="Number of Nodes:").grid(row=1, column=0, padx=10, pady=5)
        nodes_entry = tk.Entry(root)
        nodes_entry.grid(row=1, column=1, padx=10, pady=5)
        nodes_entry.insert(0, "20")

        tk.Label(root, text="Number of Links:").grid(row=2, column=0, padx=10, pady=5)
        links_entry = tk.Entry(root)
        links_entry.grid(row=2, column=1, padx=10, pady=5)
        links_entry.insert(0, "30")

        tk.Label(root, text="Topology:").grid(row=3, column=0, padx=10, pady=5)
        topology_var = tk.StringVar(value='random')
        tk.OptionMenu(root, topology_var, 'grid', 'random', 'cluster').grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Protocol:").grid(row=4, column=0, padx=10, pady=5)
        protocol_var = tk.StringVar(value='AODV')
        tk.OptionMenu(root, protocol_var, 'AODV', 'DSR').grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Steps:").grid(row=5, column=0, padx=10, pady=5)
        steps_entry = tk.Entry(root)
        steps_entry.grid(row=5, column=1, padx=10, pady=5)
        steps_entry.insert(0, "10")

        log_text = tk.StringVar()
        log_label = tk.Label(root, textvariable=log_text, justify="left")
        log_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        run_button = tk.Button(root, text="Run Simulation", command=run_simulation_gui)
        run_button.grid(row=8, columnspan=2, padx=10, pady=10)

        root.mainloop()
