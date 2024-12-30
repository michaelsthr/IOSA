from schedulers.scheduler import Scheduler
from process import LLF_Process
from plotter import Plotter
from colorama import Fore


class LeastLaxityFirst(Scheduler):
    def __init__(self):
        super().__init__()

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

        self.scheduled = sorted(self.processes, key=lambda x: x.laxity, reverse=False)
        print(f"{Fore.CYAN}Least Laxity First:\n{Fore.RESET}")
        print("Processes:")

        for process in self.processes:
            print(process)

        print("After laxity sorted Processes:")

        for process in self.scheduled:
            print(process)

        # calculate the combined relativ waiting time for each process
        self.ave_waiting_time = 0
        added_waiting_time = 0
        rel_waiting_time = 0
        for i in self.scheduled:
            rel_waiting_time += i.exec_time
            added_waiting_time += rel_waiting_time
            print("+", rel_waiting_time)

        # calculate and print the average waiting time
        print(added_waiting_time, " / ", len(self.scheduled))
        self.ave_waiting_time = added_waiting_time / len(self.scheduled)
        print("Average waiting time:", self.ave_waiting_time)
        return self.ave_waiting_time, self.scheduled

    def plot(self):
        legend_labels = [f"{p.name}, exec_time={p.exec_time}, laxity={p.laxity}" for p in self.processes]
        self.plotter = Plotter(
            processes=self.processes,
            sorted_processes=self.scheduled,
            ave_waiting_time=self.ave_waiting_time,
            title="Least Laxity First",
        )
        self.plotter.plot(legend_labels=legend_labels)
