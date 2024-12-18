from process import Process
import schedulers.sjf as sjf
import matplotlib.pyplot as plt
import random
import numpy as np

# TODO:
# The best solution would be to write a Plotter class...
# This plotter class behaves for every Scheduler differently
# I want to call it like this:
# myplotter = Plotter(sjf)
# myplotter.plot()
# (schedule() is called in plot()


def plot(processes: list, sorted_processes: list, *args, w=12, h=4):
    print(f"Plot by: {args}")

    _, axis = plt.subplots(figsize=(w, h))

    colors = ['#%06X' % random.randint(0, 0xFFFFFF)
              for _ in range(len(sorted_processes))]

    names = [p.name for p in sorted_processes]
    value = [p.get_attribute(args[0]) for p in sorted_processes]
    rel_sum = [sum(value[:i]) for i in range(len(value))]

    bars = axis.barh(names, value, left=rel_sum, color=colors)
    axis.bar_label(bars, labels=rel_sum, label_type='edge', padding=5)
    axis.bar_label(bars, labels=names, label_type='center')

    axis.set_xlabel('Time')
    axis.set_xlim(0, max(rel_sum)+max(value)+1)
    axis.invert_yaxis()

    legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in processes]
    legend_colors = [colors[sorted_processes.index(p)] for p in processes]
    legend_patches = [plt.Line2D([0], [0], color=color, lw=5)
                      for color in legend_colors]

    axis.legend(legend_patches, legend_labels,
                loc="upper right", title="Processes")

    plt.xticks(np.arange(0, max(rel_sum)+max(value)+1, step=1))
    plt.yticks([])
    plt.grid(color='grey', linestyle='-', linewidth=0.1, axis="x")
    plt.title(args[1])
    plt.text(0.5, -0.2, f"average waiting time: {args[2]}", ha='center',
             va='center', transform=axis.transAxes)

    plt.tight_layout()
    plt.show()

# TODO: REFACTOR!!!
# DO NOT USE ARGS!!! ?
if __name__ == "__main__":
    # Example to show the functionality
    p1 = Process(name="p1", exec_time=22)
    p3 = Process(name="p3", exec_time=3)
    p4 = Process(name="p4", exec_time=5)
    p2 = Process(name="p2", exec_time=2)
    p5 = Process(name="p5", exec_time=8)

    processes = [p1, p2, p3, p4, p5]
    ave_waiting_time, sorted_processes = sjf.schedule(processes)

    plot(processes, sorted_processes, "exec_time",
         "Shortest Job First", ave_waiting_time)
