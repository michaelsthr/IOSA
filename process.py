class Process:
    def __init__(self, name=None, exec_time=None, start_time=None, complet_time=None):
        self.name = name
        self.exec_time = exec_time
        self.start_time = start_time
        self.complet_time = complet_time

    def get_attribute(self, attr_name: str):
        """Returns the value of the specified attribute."""
        return getattr(self, attr_name, None)

    def __str__(self):
        """Returns a string of the object's attributes with non-None values."""
        return "".join(f"{key}: {value}\n"
            for key, value in vars(self).items() if value is not None
        )
    
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

class SJF_Process(Process):
    pass

class RoundRobin_Process(Process):
    def __init__(self, exec_time, left_exec_time, name=None):
        self.exec_time = exec_time
        self.left_exec_time = left_exec_time
        self.name = name