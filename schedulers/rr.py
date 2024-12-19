from process import RoundRobin_Process
from plotter import Plotter

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

class RoundRobin:
    def __init__(self):
        self.rr_list = [RoundRobin_Process(exec_time=22, name='P1'),
           RoundRobin_Process(exec_time=2, name='P2'),
           RoundRobin_Process(exec_time=3, name='P3'),
           RoundRobin_Process(exec_time=5, name='P4'),
           RoundRobin_Process(exec_time=8, name = 'P5')]


    def schedule(self) -> float:
        print("Round Robin:\n")
        
        copy_list = self.rr_list.copy()
        quantum = int(input("Put in the quantum: "))
        print(f'\nCalculation for quantum {quantum}:')
        scheduled = []
        clock = 0
        sum_finish_time = 0
        while copy_list:
            len_copy_list = len(copy_list)
            for i in range(len_copy_list):
                if (copy_list[i].left_exec_time > quantum):
                    copy_list[i].left_exec_time -= quantum
                    scheduled.append((copy_list[i].name,quantum))
                    clock += quantum
                    # print(scheduled[-1])
                else:
                    scheduled.append((copy_list[i].name, copy_list[i].left_exec_time))
                    clock += scheduled[-1][1]
                    print(scheduled[-1], f'-> popped at timestamp {clock}')
                    sum_finish_time += clock
                    copy_list[i].left_exec_time = 0
                    
            copy_list = [x for x in copy_list if x.left_exec_time > 0]

        ave_waiting_time = sum_finish_time / len(self.rr_list)
        print('Average waiting time:', ave_waiting_time)
        return ave_waiting_time
    
    def plot(self):
        self.plotter = Plotter(self.rr_list, title="Round Robin")
        self.plotter.plot()
    