# Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

from schedulers.shortest_job import NPShortestJobFirst, PShortestJobFirst
from schedulers.least_laxity import LeastLaxityFirst
from schedulers.first_come_first_serve import FirstComeFirstServe
from schedulers.earliest_deadline import EarliestDeadlineFirst
from schedulers.round_robin import RoundRobin
from process import Process, RoundRobin_Process, LLF_Process

import matplotlib.pyplot as plt
from colorama import Fore
from art import tprint

if __name__ == "__main__":
    tprint("IOSA")
    print("-" * 40)
    print(f"{Fore.CYAN}Welcome to IOSA - Implementation Of Scheduling Algorithms{Fore.RESET}")
    print(f"{Fore.GREEN}Made by: Matthi, Samu, Michi{Fore.RESET}")
    print("-" * 40)

    def llf():
        """Least Laxity First"""
        llf = LeastLaxityFirst()
        processes = [
            LLF_Process(name="p1", ready_time=0, deadline=10, exec_time=8),
            LLF_Process(name="p2", ready_time=0, deadline=9, exec_time=5),
            LLF_Process(name="p3", ready_time=0, deadline=9, exec_time=4),
        ]
        llf.read_processes(processes)
        llf.schedule()
        llf.plot()
        plt.show()

    def edf():
        """Earliest Deadline First"""
        edf = EarliestDeadlineFirst()
        processes = [
            Process(name="p1", deadline=9, exec_time=4),
            Process(name="p2", deadline=9, exec_time=5),
            Process(name="p3", deadline=10, exec_time=8),
        ]
        edf.read_processes(processes)
        edf.schedule()
        edf.plot()
        plt.show()

    def sjf():
        """Non Preemptive Shortest Job First"""
        sjf = NPShortestJobFirst()
        sjf.read_input("input/sjf/input0.txt", Process)
        sjf.schedule()
        sjf.plot()
        plt.show()

    def psjf():
        """Preemptive Shortest Job First"""
        sjf = PShortestJobFirst()
        sjf.read_input("input/sjf/input0.txt", Process)
        sjf.schedule()

        sjf.plot()
        plt.show()

    def fcfs():
        """First Come First Serve"""
        fcfs = FirstComeFirstServe()
        processes = [
            Process(name="p1", exec_time=22),
            Process(name="p2", exec_time=2),
            Process(name="p3", exec_time=3),
            Process(name="p4", exec_time=5),
            Process(name="p5", exec_time=8),
        ]
        fcfs.read_processes(processes)
        fcfs.schedule()

        fcfs.plot()
        plt.show()

    def rr():
        """Round Robin"""
        rr = RoundRobin()
        rr.read_input("input/rr/input0.txt", RoundRobin_Process)
        rr.schedule()

        rr.plot()
        plt.show()

    # Specific permutation examples for the project

    def ex2():
        """Permutation Example for exercice 2"""
        rr_scheduler_list = []

        for i in range(5):
            rr_scheduler = RoundRobin(3)
            rr_scheduler.read_input(f"input/rr/input{i}.txt", RoundRobin_Process)
            rr_scheduler_list.append(rr_scheduler)

        for permutation in rr_scheduler_list:
            print("-" * 40)
            print(permutation.input_path)
            permutation.schedule()
            permutation.plot()

        # Would be to much plots at once --> Try comp_sjf()
        # plt.show()

    def ex3():
        """Permutation Example for exercice 3"""
        user_input = input(f"Type 'P' for a Preemptive SJF and 'NP' for a NON Preemptive SJF:\n --> ")
        if user_input == "P":
            sjf_scheduler_class = PShortestJobFirst
        elif user_input == "NP":
            sjf_scheduler_class = NPShortestJobFirst
        else:
            raise Exception("Wrong user input")

        sjf_scheduler_list = []

        for i in range(5):
            input_file = f"input/sjf/input{i}.txt"
            sjf_scheduler = sjf_scheduler_class()
            sjf_scheduler.read_input(input_file, Process)
            sjf_scheduler_list.append(sjf_scheduler)

        for permutation in sjf_scheduler_list:
            print("-" * 40)
            print(permutation.input_path)
            permutation.schedule()
            permutation.plot()

        # Would be to much plots at once --> Try comp_sjf()
        # plt.show()

    def comp_sjf():
        """Function to compare Preemptive Shortest Job first and Non Preemptive shortest Job First at once"""

        p_sjf_scheduler = PShortestJobFirst()
        p_sjf_scheduler.read_input("input/sjf/input0.txt", Process)
        p_sjf_scheduler.schedule()
        p_sjf_scheduler.plot()

        p_sjf_scheduler = NPShortestJobFirst()
        p_sjf_scheduler.read_input("input/sjf/input0.txt", Process)
        p_sjf_scheduler.schedule()
        p_sjf_scheduler.plot2()

        plt.show()

    while True:
        try:
            schedulers = ["sjf", "psjf", "fcfs", "edf", "llf", "rr", "ex2", "ex3", "comp_sjf"]
            print("-" * 40)
            user_input = input(f"Choose a scheduler from {schedulers}\n" f"or type 'exit' to quit:\n --> ").strip().lower()
            if user_input in schedulers:
                print("-" * 40)
                exec(f"{user_input}()")
            elif user_input == "exit":
                exit()
            else:
                print("Invalid scheduler!")
        except Exception as ex:
            print(f"{Fore.YELLOW}An unexpected error occured: {ex}\n" f"But you can try other schedulers :){Fore.RESET}\n")
