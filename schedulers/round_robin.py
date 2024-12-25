from schedulers.scheduler import Scheduler
from process import RoundRobin_Process
from plotter import Plotter

from colorama import Fore
import re


class RoundRobin(Scheduler):
    def __init__(self, quantum = None):
        super().__init__()
        self.quantum = quantum

    def read_input(self, input_path: str):
        """
        Reads input from a file and populates the rr_list with RoundRobin_Process instances.
        Args:
            input_path (str): The path to the input file.
        Raises:
            ValueError: If the input file contains lines that do not match the expected format.
        Expected format for each line in the input file:
            name=<process_name>, exec_time=<execution_time>
        """
        self.processes = []
        with open(input_path) as f:
            data = f.readlines()
        for line in data:
            pattern = r"name=(\w+),\s+exec_time=(\d+)"
            match = re.search(pattern, line)

            if match is None:
                raise ValueError(f"Input '{input_path}' has invalid format:"
                                 "expected format is name=<process_name>, exec_time=<execution_time>")
            
            self.processes.append(RoundRobin_Process(int(match.group(2)), str(match.group(1))))

    def schedule(self) -> float:
        """
        Perform Round Robin scheduling.
        """
        print(f"{Fore.CYAN}Round Robin:\n{Fore.RESET}")

        self.check_processes()
        if not self.quantum:
            self.quantum = int(input("Put in the quantum: "))

        processes_to_schedule = self.processes.copy()
        print(f'Calculation for quantum {self.quantum}:')

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
                    print(f'{process.name} finished at timestamp {clock}')

            processes_to_schedule = [p for p in processes_to_schedule if p.left_exec_time > 0]

        self.average_waiting_time = sum_finish_time / len(self.processes)
        print('Average waiting time:', self.average_waiting_time)

        return self.average_waiting_time

    def plot(self):
        """
        Visualize the scheduling result.
        """
        self.check_processes()
        legend_labels = [f"{p.name}, Q={self.quantum}, exec_time={p.exec_time}"
                         for p in self.processes]
        self.plotter = Plotter(processes=self.processes,
                               sorted_processes=self.scheduled,
                               ave_waiting_time=self.average_waiting_time,
                               title="Round Robin")
        self.plotter.plot_round_robin(legend_labels)
