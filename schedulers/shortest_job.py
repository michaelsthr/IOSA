from plotter import Plotter
from schedulers.scheduler import Scheduler
from colorama import Fore


class ShortestJobFirst(Scheduler):
    def __init__(self):
        super().__init__()

    def schedule(self):
        print(f"{Fore.CYAN}Shortest Job First:\n{Fore.RESET}")

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

        return self.ave_waiting_time, self.sorted_processes

    def plot(self):
        legend_labels = [f"{p.name}, exec_time={p.exec_time}" 
                         for p in self.processes]
        self.plotter = Plotter(processes=self.processes,
                               sorted_processes=self.sorted_processes,
                               ave_waiting_time=self.ave_waiting_time,
                               title="Shortest Job First")

        self.plotter.plot(legend_labels=legend_labels)
