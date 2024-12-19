from process import EDF_Process
from plotter import Plotter


class EarliestDeadlineFirst:
    def __init__(self):
        self.edf_list = [EDF_Process(name="p1", deadline=9, exec_time=4),
                        EDF_Process(name="p2", deadline=9, exec_time=5),
                        EDF_Process(name="p3", deadline=10, exec_time=8)]

    def schedule(self) -> float:
        print('Earliest Deadline First:\n')

        # sorted list only by deadlines, not by execution times
        self.sorted_edf_list = sorted(self.edf_list, key=lambda process: process.deadline)

        for idx in range(len(self.sorted_edf_list)):
            print('  Execution time process', (idx+1), ':', self.edf_list[idx].exec_time)

        self.ave_waiting_time = 0
        added_waiting_time = 0
        rel_waiting_time = 0
        for i in self.sorted_edf_list:
            rel_waiting_time = rel_waiting_time + i.exec_time
            added_waiting_time += rel_waiting_time
            print('+', rel_waiting_time)

        print(added_waiting_time, ' / ', len(self.sorted_edf_list))
        self.ave_waiting_time = added_waiting_time / len(self.sorted_edf_list)
        print('Average waiting time:', self.ave_waiting_time)
        print('='*40, end="\n")
        return self.ave_waiting_time, self.sorted_edf_list
    
    def plot(self):
        self.plotter = Plotter(self.edf_list,  self.sorted_edf_list, title="Earliest Deadline First")
        self.plotter.plot("exec_time", self.ave_waiting_time)
