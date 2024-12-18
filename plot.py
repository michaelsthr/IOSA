from process import Process
from schedulers.sjf import schedule
import matplotlib.pyplot as plt
import random
import numpy as np


def plot(processes, sorted_processes):
    _, axis = plt.subplots(figsize=(12, 4))

    colors = ['#%06X' % random.randint(0, 0xFFFFFF)
              for _ in range(len(sorted_processes))]

    names = [p.name for p in sorted_processes]
    exec_times = [p.exec_time for p in sorted_processes]
    rel_sum = [sum(exec_times[:i]) for i in range(len(exec_times))]

    plt.grid(color='grey', linestyle='-', linewidth=0.1, axis="x")
    bars = axis.barh(names, exec_times, left=rel_sum, color=colors)
    axis.set_xlabel('Time')
    axis.set_ylabel('Processes')
    axis.invert_yaxis()

    axis.bar_label(bars, labels=rel_sum, label_type='edge', padding=5)

    plt.xticks(np.arange(0, max(rel_sum)+max(exec_times)+1, step=1))
    axis.set_xlim(0, max(rel_sum)+max(exec_times)+1)
    plt.tight_layout()

    legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in processes]
    legend_colors = [colors[sorted_processes.index(p)] for p in processes]
    legend_patches = [plt.Line2D([0], [0], color=color, lw=5)
                      for color in legend_colors]
    axis.legend(legend_patches, legend_labels, loc='upper right')

    plt.show()


if __name__ == "__main__":
    # Example to show the functionality
    p1 = Process(name="p1", exec_time=22)
    p3 = Process(name="p3", exec_time=3)
    p4 = Process(name="p4", exec_time=5)
    p2 = Process(name="p2", exec_time=2)
    p5 = Process(name="p5", exec_time=8)

    processes = [p1, p2, p3, p4, p5]
    _, sorted_ = schedule(processes)

    plot(processes, sorted_)
