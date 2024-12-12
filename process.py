class Process:
    def __init__(self, name=None, ready_time=None, exec_time=None, deadline=None, start_time=None, complet_time=None):
        self.name = name
        self.ready_time = ready_time
        self.exec_time = exec_time
        self.deadline = deadline
        self.start_time = start_time
        self.complet_time = complet_time

    def __str__(self):
        """Returns a string of the object's attributes with non-None values."""
        return "".join(f"{key}: {value}\n"
            for key, value in vars(self).items() if value is not None
        )
    
class FCFS_Process(Process):
    pass

class EDF_Process(Process):
    def __init__(self, exec_time, deadline, name=None):
        pass

class LLF_Process(Process):
    def __init__(self, ready_time, exec_time, deadline, laxity, name=None):
        self.calc_laxity()

    def calc_laxity(self):
        self.laxity = (self.deadline - self.ready_time) - self.exec_time

class SJF_Process(Process):
    pass

class RoundRobin_Process(Process):
    def __init__(self, exec_time, left_exec_time, name=None):
        pass