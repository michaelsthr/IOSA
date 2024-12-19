from process import RoundRobin_Process
from plotter import Plotter


class RoundRobin:
    def __init__(self):
        self.rr_list = [RoundRobin_Process(exec_time=22, name='P1'),
                        RoundRobin_Process(exec_time=2, name='P2'),
                        RoundRobin_Process(exec_time=3, name='P3'),
                        RoundRobin_Process(exec_time=5, name='P4'),
                        RoundRobin_Process(exec_time=8, name='P5')]

    def schedule(self) -> float:
        print("Round Robin:\n")

        copy_list = self.rr_list.copy()
        quantum = int(input("Put in the quantum: "))
        print(f'\nCalculation for quantum {quantum}:')
        scheduled = []
        clock = 0
        sum_finish_time = 0
        while copy_list:
            for process in copy_list:
                if (process.left_exec_time > quantum):
                    process.left_exec_time -= quantum
                    scheduled.append((process.name, quantum))
                    clock += quantum
                else:
                    scheduled.append((process.name, process.left_exec_time))
                    quantum = scheduled[-1][1]
                    clock += quantum
                    print(scheduled[-1], f'-> popped at timestamp {clock}')
                    sum_finish_time += clock
                    process.left_exec_time = 0

            copy_list = [x for x in copy_list if x.left_exec_time > 0]

        ave_waiting_time = sum_finish_time / len(self.rr_list)
        print('Average waiting time:', ave_waiting_time)

        print(scheduled)
        return ave_waiting_time

    def plot(self):
        self.plotter = Plotter(self.rr_list, title="Round Robin")
        self.plotter.plot()
