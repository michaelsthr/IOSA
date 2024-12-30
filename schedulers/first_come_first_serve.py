# Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

from schedulers.scheduler import Scheduler
from plotter import Plotter
from colorama import Fore


class FirstComeFirstServe(Scheduler):
    def __init__(self):
        super().__init__()

    def schedule(self) -> float:
        '''
        Perform the First Come First Serve scheduler.
        '''
        print(f"{Fore.CYAN}First Come First Serve:\n{Fore.RESET}")
        print("Processes:\nExecution-Times:")

        # print the details of the input processes
        for idx in range(len(self.processes)):
            print("  Execution time process", (idx + 1), ":", self.processes[idx].exec_time)

        self.scheduled = self.processes

        # calculate the combined relativ waiting time for each process
        self.ave_waiting_time = 0
        added_waiting_time = 0
        rel_waiting_time = 0
        for i in self.processes:
            rel_waiting_time += i.exec_time
            added_waiting_time += rel_waiting_time
            print("+", rel_waiting_time)

        # calculate and print the average waiting time
        print(added_waiting_time, " / ", len(self.processes))
        self.ave_waiting_time = added_waiting_time / len(self.processes)
        print("Average waiting time:", self.ave_waiting_time)
        return self.ave_waiting_time, self.processes

    def plot(self):
        legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in self.processes]
        self.plotter = Plotter(
            processes=self.processes,
            sorted_processes=self.processes,
            ave_waiting_time=self.ave_waiting_time,
            title="First Come First Serve",
        )
        self.plotter.plot(legend_labels=legend_labels)
