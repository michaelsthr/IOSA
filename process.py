class Process:
    def __init__(self, ready_time=None, exec_time=None, deadline=None, start_time=None, complet_time=None):
        self.ready_time = ready_time
        self.exec_time = exec_time
        self.deadline = deadline
        self.start_time = start_time
        self.complet_time = complet_time


    def __str__(self):
        return f"{self.ready_time}, {self.exec_time}, {self.deadline}, {self.start_time}, {self.complet_time}"