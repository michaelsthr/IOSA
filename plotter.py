from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import random
import numpy as np

class Plotter():
    # TODO: Enable more options for the legend
    def __init__(self, processes: list, sorted_processes: list, title="Scheduler-Plotter"):
        self.processes = processes
        self.sorted_processes = sorted_processes
        self.title = title

    def plot(self, *args, w=12, h=4):
        _, axis = plt.subplots(figsize=(w, h))

        names = [p.name for p in self.sorted_processes]
        value = [p.get_attribute(args[0]) for p in self.sorted_processes]
        rel_sum = [sum(value[:i]) for i in range(len(value))]
        colors = ['#%06X' % random.randint(0, 0xFFFFFF)
                  for _ in range(len(self.sorted_processes))]

        bars = axis.barh(names, value, left=rel_sum, color=colors)
        axis.bar_label(bars, labels=rel_sum, label_type='edge', padding=5)
        axis.bar_label(bars, labels=names, label_type='center')

        axis.set_xlabel('Time')
        axis.set_xlim(0, max(rel_sum)+max(value)+1)
        axis.invert_yaxis()

        legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in self.processes]
        legend_colors = [colors[self.sorted_processes.index(p)] for p in self.processes]
        legend_patches = [plt.Line2D([0], [0], color=color, lw=5) for color in legend_colors]

        axis.legend(legend_patches, legend_labels,loc="upper right", title="Processes")

        plt.xticks(np.arange(0, max(rel_sum)+max(value)+1, step=1))
        plt.yticks([])
        plt.grid(color='grey', linestyle='-', linewidth=0.1, axis="x")
        plt.title(self.title)
        plt.text(0.5, -0.2, f"average waiting time: {args[1]}", ha='center', va='center', transform=axis.transAxes)

        plt.tight_layout()
        plt.show()
