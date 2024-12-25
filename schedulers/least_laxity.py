from process import LLF_Process
from plotter import Plotter
from colorama import Fore

class LeastLaxityFirst:
    def __init__(self):
        self.llf_list = [LLF_Process(name="p1", ready_time=0, deadline=10, exec_time=8),
                    LLF_Process(name="p2", ready_time=0, deadline=9, exec_time=5), 
                    LLF_Process(name="p3", ready_time=0, deadline=9, exec_time=4)]

    def schedule(self) -> float:
        # The output will be like this:

        # Least Laxity First:

        # Processes:
        # + 22
        # + 24
        # + 27
        # + 32
        # + 40
        # 145  /  5
        # Average waiting time: 29.0

        self.sorted_after_lax = sorted(self.llf_list, key=lambda x: x.laxity, reverse=False)
        print(f'{Fore.CYAN}Least Laxity First:\n{Fore.RESET}')
        print('Processes:')

        for process in self.llf_list:
            print(process)

        print("After laxity sorted Processes:")

        for process in self.sorted_after_lax:
            print(process)

        # calculate the combined relativ waiting time for each process
        self.ave_waiting_time = 0
        added_waiting_time = 0
        rel_waiting_time = 0
        for i in self.sorted_after_lax:
            rel_waiting_time += i.exec_time
            added_waiting_time += rel_waiting_time
            print('+', rel_waiting_time)
            
        # calculate and print the average waiting time
        print(added_waiting_time, ' / ', len(self.sorted_after_lax))
        self.ave_waiting_time = added_waiting_time / len(self.sorted_after_lax)
        print('Average waiting time:', self.ave_waiting_time)
        return self.ave_waiting_time, self.sorted_after_lax

    def plot(self):
        legend_labels = [f"{p.name}, exec_time={p.exec_time}, laxity={p.laxity}" 
                         for p in self.llf_list]
        self.plotter = Plotter(processes=self.llf_list,
                               sorted_processes=self.sorted_after_lax,
                               ave_waiting_time=self.ave_waiting_time,
                               title="Least Laxity First")
        self.plotter.plot(legend_labels=legend_labels)