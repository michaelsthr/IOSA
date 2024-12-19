from process import SJF_Process
from plotter import Plotter


class ShortestJobFirst():
    def __init__(self):
        p1 = SJF_Process(name="p1", exec_time=22)
        p3 = SJF_Process(name="p3", exec_time=3)
        p4 = SJF_Process(name="p4", exec_time=5)
        p2 = SJF_Process(name="p2", exec_time=2)
        p5 = SJF_Process(name="p5", exec_time=8)
        processes = [p1, p2, p3, p4, p5]
        self.processes = processes

    def schedule(self):
        print("Shortest Job First:\n")

        self.sorted_processes = sorted(self.processes, key=lambda p: p.exec_time)

        for l in self.sorted_processes:
            print(l)

        # calculate the combined relativ waiting time for each process
        self.ave_waiting_time = 0
        added_waiting_time = 0
        rel_waiting_time = 0
        for i in self.sorted_processes:
            rel_waiting_time += i.exec_time
            added_waiting_time += rel_waiting_time
            print('+', rel_waiting_time)

        # calculate and print the average waiting time
        print(added_waiting_time, ' / ', len(self.sorted_processes))
        self.ave_waiting_time = added_waiting_time / len(self.sorted_processes)
        print('Average waiting time:', self.ave_waiting_time)
        print('='*40, end="\n")

        return self.ave_waiting_time, self.sorted_processes

    def plot(self):
        self.plotter = Plotter(self.processes,  self.sorted_processes, title="Shortest Job First")

        legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in self.processes]
        exec_times = [p.exec_time for p in self.sorted_processes]

        self.plotter.plot(avg_time=self.ave_waiting_time, legend_labels=legend_labels, exec_times=exec_times)
