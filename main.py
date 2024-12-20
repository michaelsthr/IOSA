from schedulers.shortest_job import ShortestJobFirst
from schedulers.least_laxity import LeastLaxityFirst
from schedulers.first_come_first_serve import FirstComeFirstServe
from schedulers.earliest_deadline import EarliestDeadlineFirst
from schedulers.round_robin import RoundRobin

from colorama import Fore, Style
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
        sjf.schedule()
        sjf.plot()

    def fcfs():
        fcfs = FirstComeFirstServe()
        fcfs.schedule()
        fcfs.plot()

    def rr():
        rr = RoundRobin()
        rr.schedule()
        # Not implemented yet
        # rr.plot()

    while True:
        try:
            schedulers = ["sjf", "fcfs", "edf", "llf", "rr"]
            print("\n")
            print("-" * 40, end="\n")
            user_input = input(f"Paste your desired scheduler {schedulers}\n"
                               "Type exit to exit :o\n"
                               " --> ").strip()
            if user_input in schedulers:
                exec(f"{user_input}()")
            elif user_input == "exit":
                exit()
            else:
                print("Invalid scheduler!")
        except Exception as ex:
            print(f"{Fore.YELLOW} An unexpected error occured: {ex}\n"
                  f"But you can try other schedulers :){Fore.RESET}\n")
