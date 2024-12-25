from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import cm


class Plotter():
    # TODO: Enable more options for the legend
    def __init__(self,
                 processes: list,
                 sorted_processes: list,
                 ave_waiting_time=0,
                 title="Scheduler-Plotter"):
        self.processes = processes
        self.sorted_processes = sorted_processes
        self.title = title
        self.ave_waiting_time = ave_waiting_time

    def plot(self, legend_labels: list, w=12, h=4):
        """
        Plots a horizontal bar chart representing process execution times.
        Parameters:
            avg_time (float): The average waiting time to be displayed on the plot.
            legend_labels (list): A list of labels for the legend.
            >>> legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in self.edf_list]

            exec_times (list): A list of execution times for the processes.
            >>> exec_times = [p.exec_time for p in self.sorted_edf_list]

            w (int, optional): The width of the plot. Default is 12.
            h (int, optional): The height of the plot. Default is 4.
        """
        _, axis = plt.subplots(figsize=(w, h))

        process_times = [p.exec_time for p in self.sorted_processes]
        process_names = [p.name for p in self.sorted_processes]
        relative_cumulative_sum = [sum(process_times[:i]) for i in range(len(process_times))]

        # Generate color map
        cmap = cm.get_cmap('Set3', len(self.sorted_processes))
        colors = [cmap(i) for i in range(len(self.sorted_processes))]
        legend_colors =  [colors[self.sorted_processes.index(p)] for p in self.processes]

        # Place bars and labels
        bars = axis.barh(process_names, process_times,
                         left=relative_cumulative_sum, color=colors, edgecolor='black')
        axis.bar_label(bars, labels=process_names, label_type='center')
        axis.set_xlabel('Time')
        axis.set_xlim(0, max(relative_cumulative_sum)+max(process_times)+1)
        axis.invert_yaxis()

        legend_patches = [plt.Line2D([0], [0], color=color, lw=5) for color in legend_colors]
        axis.legend(legend_patches, legend_labels,
                    loc="upper right", title="Processes")

        plt.xticks(np.arange(0, max(relative_cumulative_sum) +
                   max(process_times)+1, step=1))
        plt.yticks([])
        plt.grid(color='grey', linestyle='-', linewidth=0.1, axis="x")
        plt.title(self.title)
        plt.text(0.5, -0.2, f"average waiting time: {round(
            self.ave_waiting_time, 2)}", ha='center', va='center', transform=axis.transAxes)

        plt.tight_layout()
        plt.show()

    def plot_round_robin(self, legend_labels: list, w=12, h=6):
        """Specialized plotter function for round robin"""

        # Extract values from round robin tuples: ("P1", 3)
        data_names = [p[0] for p in self.sorted_processes]
        data_times = [p[1] for p in self.sorted_processes]
        process_names = [p.name for p in self.processes]

        # Create color maps and map with a dictionary
        colors_list = cm.Set3.colors
        colors_dict = {name: colors_list[i % len(
            colors_list)] for i, name in enumerate(process_names)}
        colors = [colors_dict[name] for name in data_names]

        # Addition of every element in data
        cumulative_sum = np.cumsum([0] + data_times[:-1])

        # Create plot and bars
        _, axis = plt.subplots(figsize=(w, h))
        bars = axis.barh(0, data_times, left=cumulative_sum,
                         color=colors, edgecolor='black')
        axis.bar_label(bars, labels=data_names, label_type="center")
        axis.get_yaxis().set_visible(False)
        axis.set_xlabel('Time')
        plt.text(0.5, -0.2, f"average waiting time: {round(self.ave_waiting_time, 2)}",
                 ha='center', va='center', transform=axis.transAxes)
        plt.xticks(np.arange(0, max(cumulative_sum)+max(data_times)-1, step=1))

        # Create legend
        handles = [plt.Line2D([0], [0], color=colors_dict[name], lw=4)
                   for name in process_names]
        axis.legend(handles, legend_labels,
                    title="Processes", loc="upper right")
        axis.set_title(self.title)

        plt.grid(color='grey', linestyle='-', linewidth=0.1, axis="x")
        plt.tight_layout()
        plt.show()
