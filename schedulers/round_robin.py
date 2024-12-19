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
        self.quantum = int(input("Put in the quantum: "))
        print(f'\nCalculation for quantum {self.quantum}:')
        self.scheduled = []
        clock = 0
        sum_finish_time = 0
        while copy_list:
            for process in copy_list:
                if (process.left_exec_time > self.quantum):
                    process.left_exec_time -= self.quantum
                    self.scheduled.append((process.name, self.quantum))
                    clock += self.quantum
                else:
                    self.scheduled.append(
                        (process.name, process.left_exec_time))
                    clock += self.scheduled[-1][1]
                    print(self.scheduled[-1],
                          f'-> popped at timestamp {clock}')
                    sum_finish_time += clock
                    process.left_exec_time = 0

            copy_list = [x for x in copy_list if x.left_exec_time > 0]

        self.ave_waiting_time = sum_finish_time / len(self.rr_list)
        print('Average waiting time:', self.ave_waiting_time)

        print(self.scheduled)
        return self.ave_waiting_time

    def plot(self):
        legend_labels = [f"{p.name}, Q={self.quantum}, exec_time={p.exec_time}"
                         for p in self.rr_list]

        self.plotter = Plotter(processes=self.rr_list,
                               sorted_processes=self.scheduled,
                               ave_waiting_time=self.ave_waiting_time,
                               title="Round Robin")

        self.plotter.plot_round_robin(legend_labels)
