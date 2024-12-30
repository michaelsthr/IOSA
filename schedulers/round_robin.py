# Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

from schedulers.scheduler import Scheduler
from process import RoundRobin_Process
from plotter import Plotter
from colorama import Fore
import re


class RoundRobin(Scheduler):
    def __init__(self, quantum=None):
        super().__init__()
        self.quantum = quantum

    def schedule(self) -> float:
        """
        Perform the Round Robin scheduling.
        """
        print(f"{Fore.CYAN}Round Robin:\n{Fore.RESET}")

        self.check_processes()
        if not self.quantum:
            self.quantum = int(input("Put in the quantum: "))

        processes_to_schedule = self.processes.copy()
        print(f"Calculation for quantum {self.quantum}:")

        clock = 0
        sum_finish_time = 0

        while processes_to_schedule:
            for process in processes_to_schedule:
                time_slice = min(process.left_exec_time, self.quantum)
                process.left_exec_time -= time_slice
                self.scheduled.append((process.name, time_slice))
                clock += time_slice

                if process.left_exec_time == 0:
                    sum_finish_time += clock
                    print(f"{process.name} finished at timestamp {clock}")

            processes_to_schedule = [p for p in processes_to_schedule if p.left_exec_time > 0]

        self.average_waiting_time = sum_finish_time / len(self.processes)
        print("Average waiting time:", self.average_waiting_time)

        return self.average_waiting_time

    def plot(self):
        """
        Visualize the scheduling result.
        """
        self.check_processes()
        legend_labels = [f"{p.name}, Q={self.quantum}, exec_time={p.exec_time}" for p in self.processes]
        self.plotter = Plotter(
            processes=self.processes,
            sorted_processes=self.scheduled,
            ave_waiting_time=self.average_waiting_time,
            title="Round Robin",
        )
        self.plotter.plot2(legend_labels)
