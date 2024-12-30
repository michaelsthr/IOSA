# Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

from process import Process
import re


class Scheduler:
    def __init__(self):
        self.processes = []
        self.scheduled = []
        self.average_waiting_time = 0

    def read_processes(self, processes: list):
        """
        Set processes
        """
        self.processes = processes

    def check_processes(self):
        """
        Checks if the round-robin list of processes is defined.
        """
        if not self.processes:
            raise ValueError("No lists for the processes defined!")

    def read_input(self, input_path: str, process_class):
        """
        Reads input from a file and populates the processes list with instances of process_class.
        Args:
            input_path (str): The path to the input file.
            process_class (class): The class to instantiate for each process.
        Raises:
            ValueError: If the input file contains lines that do not match the expected format.
        Expected format for each line in the input file:
            name=<process_name>, exec_time=<execution_time>, [optional parameters]
        """
        self.processes = []
        with open(input_path) as f:
            data = f.readlines()
        for line in data:
            matches = re.findall(r"(\w+)=(\w+)", line)

            if not matches:
                raise ValueError(f"Input '{input_path}' has invalid format")

            kwargs = {key: int(value) if value.isdigit() else value for key, value in matches}
            self.processes.append(process_class(**kwargs))

    def schedule(self):
        """
        Perform the scheduling algorithm.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def plot(self):
        """
        Visualize the scheduling result.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
