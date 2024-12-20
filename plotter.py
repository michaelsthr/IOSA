from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import cm

class Plotter():
    # TODO: Enable more options for the legend
    def __init__(self, processes: list, sorted_processes: list, title="Scheduler-Plotter"):
        self.processes = processes
        self.sorted_processes = sorted_processes
        self.title = title

    def plot(self, avg_time:float, legend_labels: list, exec_times: list, w=12, h=4):
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

        names = [p.name for p in self.sorted_processes]
        relative_cumulative_sum = [sum(exec_times[:i]) for i in range(len(exec_times))]
        
        # Generate color map
        legend_colors, colors = self.add_colors()

        # Place bars and labels
        bars = axis.barh(names, exec_times, left=relative_cumulative_sum, color=colors)
        axis.bar_label(bars, labels=names, label_type='center')
        axis.set_xlabel('Time')
        axis.set_xlim(0, max(relative_cumulative_sum)+max(exec_times)+1)
        axis.invert_yaxis()


        legend_patches = [plt.Line2D([0], [0], color=color, lw=5) for color in legend_colors]
        axis.legend(legend_patches, legend_labels,loc="upper right", title="Processes")

        plt.xticks(np.arange(0, max(relative_cumulative_sum)+max(exec_times)+1, step=1))
        plt.yticks([])
        plt.grid(color='grey', linestyle='-', linewidth=0.1, axis="x")
        plt.title(self.title)
        plt.text(0.5, -0.2, f"average waiting time: {round(avg_time, 2)}", ha='center', va='center', transform=axis.transAxes)

        plt.tight_layout()
        plt.show()

    def add_colors(self):
        """
        Generates color map and returns legend colors and colors
        Returns:
            - List of colors corresponding to the processes in the original order.
            - List of colors corresponding to the sorted processes.
        """
        cmap = cm.get_cmap('Set3', len(self.sorted_processes))
        colors = [cmap(i) for i in range(len(self.sorted_processes))]
        return [colors[self.sorted_processes.index(p)] for p in self.processes], colors
