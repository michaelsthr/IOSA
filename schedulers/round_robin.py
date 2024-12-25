import re
from process import RoundRobin_Process
from plotter import Plotter


class RoundRobin:
    def __init__(self):
        self.rr_list = None

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
        self.rr_list = []
        with open(input_path) as f:
            data = f.readlines()
        for line in data:
            pattern = r"name=(\w+),\s+exec_time=(\d+)"
            match = re.search(pattern, line)

            if match is None:
                raise ValueError(f"Input '{input_path}' has invalid format:"
                                 "expected format is name=<process_name>, exec_time=<execution_time>")
            
            self.rr_list.append(RoundRobin_Process(int(match.group(2)), str(match.group(1))))

    def read_list(self, rr_list: list):
        """
        Reads and stores a list for the round-robin scheduler.

        Args:
            rr_list (list): The list to be used by the round-robin scheduler.
        """
        self.rr_list = rr_list

    def check_list(self):
        """
        Checks if the round-robin list of processes is defined.

        Raises:
            Exception: If the round-robin list (rr_list) is None.
        """
        if self.rr_list is None:
            raise Exception("No lists for the processes defined!")

    def schedule(self) -> float:
        print("Round Robin:\n")

        self.check_list()

        copy_list = self.rr_list.copy()
        self.quantum = int(input("Put in the quantum: "))
        print(f'\nCalculation for quantum {self.quantum}:')
        self.scheduled = []
        clock = 0
        sum_finish_time = 0
        while copy_list:
            for process in copy_list:
                if (process.left_exec_time > self.quantum):
                    process.left_exec_time -= self.quantum
                    self.scheduled.append((process.name, self.quantum))
                    clock += self.quantum
                else:
                    self.scheduled.append(
                        (process.name, process.left_exec_time))
                    clock += self.scheduled[-1][1]
                    print(self.scheduled[-1],
                          f'-> popped at timestamp {clock}')
                    sum_finish_time += clock
                    process.left_exec_time = 0

            copy_list = [x for x in copy_list if x.left_exec_time > 0]

        self.ave_waiting_time = sum_finish_time / len(self.rr_list)
        print('Average waiting time:', self.ave_waiting_time)

        print(self.scheduled)
        return self.ave_waiting_time

    def plot(self):
        self.check_list()
        legend_labels = [f"{p.name}, Q={self.quantum}, exec_time={p.exec_time}"
                         for p in self.rr_list]
        self.plotter = Plotter(processes=self.rr_list,
                               sorted_processes=self.scheduled,
                               ave_waiting_time=self.ave_waiting_time,
                               title="Round Robin")
        self.plotter.plot_round_robin(legend_labels)
