from plotter import Plotter
from schedulers.scheduler import Scheduler
from colorama import Fore


class NPShortestJobFirst(Scheduler):
    """
    Non Preemptive shortest job first.
    >Can not< break process to schedule another process
    """

    def __init__(self):
        super().__init__()

    def schedule(self):
        print(f"{Fore.CYAN}Shortest Job First:\n{Fore.RESET}")

        self.scheduled = sorted(self.processes, key=lambda p: p.exec_time)

        for l in self.scheduled:
            print(l)

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
        legend_labels = [f"{p.name}, exec_time={p.exec_time}" for p in self.processes]
        self.plotter = Plotter(
            processes=self.processes,
            sorted_processes=self.scheduled,
            ave_waiting_time=self.ave_waiting_time,
            title="Non Preemptive Shortest Job First",
        )

        self.plotter.plot(legend_labels=legend_labels)

    def plot2(self):
        """
        Visualize the scheduling result.
        """
        self.check_processes()

        self.new_processes = [(p.name, p.exec_time) for p in self.scheduled]
        self.scheduled = self.new_processes.copy()

        legend_labels = [f"{p.name}, exec_time={p.exec_time}, ready_time={p.ready_time}" for p in self.processes]
        self.plotter = Plotter(
            processes=self.processes,
            sorted_processes=self.scheduled,
            ave_waiting_time=self.average_waiting_time,
            title="Preemptive Shortest Job First",
        )
        self.plotter.plot2(legend_labels)


class PShortestJobFirst(Scheduler):
    """
    Preemptive shortest job first.
    >Can< break process to schedule another process
    """

    def __init__(self):
        super().__init__()

    def schedule(self):
        print(f"{Fore.CYAN}Preemptive Shortest Job First:\n{Fore.RESET}")

        processes_to_schedule = sorted(self.processes, key=lambda p: (p.ready_time, p.exec_time)).copy()

        clock = 0
        sum_finish_time = 0

        while processes_to_schedule:
            ready_processes = [p for p in processes_to_schedule if p.ready_time <= clock]
            if not ready_processes:
                clock = processes_to_schedule[0].ready_time
                continue

            ready_processes = sorted(ready_processes, key=lambda p: p.exec_time)
            current_process = ready_processes[0]

            # I got some random error without `default=float('inf')`. Dont ask me what this is
            next_ready_time = min([p.ready_time for p in processes_to_schedule if p.ready_time > clock], default=float("inf"))
            time_slice = min(current_process.left_exec_time, next_ready_time - clock)

            current_process.left_exec_time -= time_slice
            self.scheduled.append((current_process.name, time_slice))
            clock += time_slice

            if current_process.left_exec_time == 0:
                sum_finish_time += clock
                print(f"{current_process.name} finished at timestamp {clock}")
                processes_to_schedule.remove(current_process)

        self.average_waiting_time = sum_finish_time / len(self.processes)
        print("Average waiting time:", self.average_waiting_time)

        return self.average_waiting_time

    def plot(self):
        """
        Visualize the scheduling result.
        """
        self.check_processes()
        legend_labels = [f"{p.name}, exec_time={p.exec_time}, ready_time={p.ready_time}" for p in self.processes]
        self.plotter = Plotter(
            processes=self.processes,
            sorted_processes=self.scheduled,
            ave_waiting_time=self.average_waiting_time,
            title="Preemptive Shortest Job First",
        )
        self.plotter.plot2(legend_labels)
