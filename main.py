import schedulers.fcfs as fcfs
import schedulers.sjf as sjf
import schedulers.llf as llf
import schedulers.edf as edf
import schedulers.rr as rr

if __name__ == "__main__":
    print("=" * 40)
    print("Welcome to IOSA - Implementation Of Scheduling Algorithms")
    print("Made by: Matthi, Samu, Michi")
    print("=" * 40)
    edf.schedule()
    rr.schedule()
    llf.schedule()
    
    