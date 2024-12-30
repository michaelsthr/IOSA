# Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

class Process:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.exec_time = kwargs.get("exec_time")
        self.start_time = kwargs.get("start_time")
        self.complet_time = kwargs.get("complet_time")
        self.ready_time = kwargs.get("ready_time")

        self.left_exec_time = self.exec_time

    def __str__(self):
        """Returns a string of the object's attributes with non-None values."""
        return "".join(f"{key}: {value}\n" for key, value in vars(self).items() if value is not None)


class FCFS_Process(Process):
    pass


class EDF_Process(Process):
    def __init__(self, exec_time, deadline, name=None):
        self.name = name
        self.deadline = deadline
        self.exec_time = exec_time


class LLF_Process(Process):
    def __init__(self, ready_time, exec_time, deadline, name=None):
        self.name = name
        self.ready_time = ready_time
        self.exec_time = exec_time
        self.deadline = deadline
        self.calc_laxity()

    def calc_laxity(self):
        self.laxity = (self.deadline - self.ready_time) - self.exec_time


class RoundRobin_Process(Process):
    def __init__(self, exec_time: int, name="p"):
        self.exec_time = exec_time
        self.left_exec_time = exec_time
        self.name = name
