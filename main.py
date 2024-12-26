from schedulers.shortest_job import ShortestJobFirst
from schedulers.least_laxity import LeastLaxityFirst
from schedulers.first_come_first_serve import FirstComeFirstServe
from schedulers.earliest_deadline import EarliestDeadlineFirst
from schedulers.round_robin import RoundRobin
from process import Process, RoundRobin_Process

from colorama import Fore
from art import tprint

if __name__ == "__main__":
    tprint("IOSA")
    print("-" * 40)
    print(f"{Fore.CYAN}Welcome to IOSA - Implementation Of Scheduling Algorithms{Fore.RESET}")
    print(f"{Fore.GREEN}Made by: Matthi, Samu, Michi{Fore.RESET}")
    print("-" * 40)

    # TODO: Multiple windows at once

    def llf():
        llf = LeastLaxityFirst()
        llf.schedule()
        llf.plot()

    def edf():
        edf = EarliestDeadlineFirst()
        edf.schedule()
        edf.plot()

    def sjf():
        sjf = ShortestJobFirst()
        sjf.read_input("input/sjf/input0.txt", Process)
        sjf.schedule()
        sjf.plot()

    def fcfs():
        fcfs = FirstComeFirstServe()
        fcfs.schedule()
        fcfs.plot()

    def rr():
        rr = RoundRobin()
        rr.read_input("input/rr/input0.txt", RoundRobin_Process)
        rr.schedule()
        rr.plot()

    def rr2():
        # TODO: Display all at once ...
        rr_scheduler_list = []

        for i in range(5):
            rr_scheduler = RoundRobin(3)
            rr_scheduler.read_input(f"input/rr/input{i}.txt")
            rr_scheduler_list.append(rr_scheduler)

        for permutation in rr_scheduler_list:
            print("-" * 40)
            permutation.schedule()
            permutation.plot()

    while True:
        try:
            schedulers = ["sjf", "fcfs", "edf", "llf", "rr", "rr2"]
            print("-" * 40)
            user_input = input(f"Choose a scheduler from {schedulers}\n"
                               f"or type 'exit' to quit:\n --> ").strip().lower()
            if user_input in schedulers:
                print("-" * 40)
                exec(f"{user_input}()")
            elif user_input == "exit":
                exit()
            else:
                print("Invalid scheduler!")
        except Exception as ex:
            print(f"{Fore.YELLOW} An unexpected error occured: {ex}\n"
                  f"But you can try other schedulers :){Fore.RESET}\n")
