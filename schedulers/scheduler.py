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

    def read_input(self, input_path: str):
        """
        Read input data from a given source and set self.processes.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

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