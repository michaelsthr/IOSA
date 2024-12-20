from process import FCFS_Process
from plotter import Plotter

class FirstComeFirstServe:
    def __init__(self):
        self.fcfs_list = [FCFS_Process(name="p1", exec_time=22),
                          FCFS_Process(name="p2", exec_time=2),
                          FCFS_Process(name="p3", exec_time=3),
                          FCFS_Process(name="p4", exec_time=5),
                          FCFS_Process(name="p5", exec_time=8)]

    def schedule(self) -> float:
        # The output will be like this:

        # First Come First Serve:

        # Processes:
        # Execution-Times:
        # Execution time process 1 : 22
        # Execution time process 2 : 2
        # Execution time process 3 : 3
        # Execution time process 4 : 5
        # Execution time process 5 : 8
        # + 22
        # + 24
        # + 27
        # + 32
        # + 40
        # 145  /  5
        # Average waiting time: 29.0

        print('First Come First Serve:\n')
        print('Processes:\nExecution-Times:')

        # print the details of the input processes
        for idx in range(len(self.fcfs_list)):
            print('  Execution time process', (idx+1),
                  ':', self.fcfs_list[idx].exec_time)

        # calculate the combined relativ waiting time for each process
        self.ave_waiting_time = 0
        added_waiting_time = 0
        rel_waiting_time = 0
        for i in self.fcfs_list:
            rel_waiting_time += i.exec_time
            added_waiting_time += rel_waiting_time
            print('+', rel_waiting_time)

        # calculate and print the average waiting time
        print(added_waiting_time, ' / ', len(self.fcfs_list))
        self.ave_waiting_time = added_waiting_time / len(self.fcfs_list)
        print('Average waiting time:', self.ave_waiting_time)
        print('='*40, end="\n")
        return self.ave_waiting_time, self.fcfs_list
    
    def plot(self):
        self.plotter = Plotter(self.fcfs_list,  self.fcfs_list, title="First Come First Serve")

        legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in self.fcfs_list]
        exec_times = [p.exec_time for p in self.fcfs_list]

        self.plotter.plot(avg_time=self.ave_waiting_time, legend_labels=legend_labels, exec_times=exec_times)
