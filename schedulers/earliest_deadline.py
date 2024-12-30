# Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

from plotter import Plotter
from colorama import Fore
from schedulers.scheduler import Scheduler


class EarliestDeadlineFirst(Scheduler):
    def __init__(self):
        super().__init__()

    def schedule(self) -> float:
        '''
        Perform the Earliest Deadline First scheduler.
        '''
        print(f"{Fore.CYAN}Earliest Deadline First:\n{Fore.RESET}")

        print("Processes with deadlines:")
        for p in self.processes:
            print(p)

        # sorted list only by deadlines, not by execution times
        self.scheduled = sorted(self.processes, key=lambda process: process.deadline)

        self.ave_waiting_time = 0
        added_waiting_time = 0
        rel_waiting_time = 0
        for i in self.scheduled:
            rel_waiting_time = rel_waiting_time + i.exec_time
            added_waiting_time += rel_waiting_time
            print("+", rel_waiting_time)

        print(added_waiting_time, " / ", len(self.scheduled))
        self.ave_waiting_time = added_waiting_time / len(self.scheduled)
        print("Average waiting time:", self.ave_waiting_time)
        return self.ave_waiting_time, self.scheduled

    def plot(self):
        legend_labels = [f"{p.name}, exec_time={p.exec_time}, deadline={p.deadline}" for p in self.processes]

        self.plotter = Plotter(
            processes=self.processes,
            sorted_processes=self.scheduled,
            ave_waiting_time=self.ave_waiting_time,
            title="Earliest Deadline First",
        )

        self.plotter.plot(legend_labels=legend_labels)
