# IOSA - Implementation Of Scheduling Algorithms
### Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

### Implementations of following algorithms:
- FCFS: First-Come-First-Serve schedules processes in the order they arrive in the ready queue. 
    - It is simple but can lead to the convoy effect.
- SJF non-preemptive: Shortest Job First selects the process with the smallest execution time. 
    - It minimizes average waiting time but requires precise knowledge of execution times.
- SJF preemptive: Similar to the non-preemptive approach, but with the difference, that the running process gets interrupted, when a new process is ready. Now the new shortest-job gets selected again.
    - In the case, that not all processes are ready from the start, the average waiting time is smaller than with the non-preemptive approach
- EDF: Earliest Deadline First prioritizes processes with the closest deadlines.
    - It is optimal for real-time systems but can be complex to implement.
- LLF: Least Laxity First schedules processes based on their laxity, which is the difference between their deadline and remaining execution time.
    - It aims to prevent deadline misses.
- Round Robin with Quantum Q: Round Robin assigns a fixed time quantum to each process in a cyclic order. 
    - It ensures fairness but can lead to high context-switching overhead.
 


### Working
- All schedulers are working and can be plotted
- SJF and RR use input.txt files to read the processes

### Installation
To install Python, download and install it from [python.org](https://www.python.org/).
To install the required dependencies, run the following command:
```sh
pip install -r requirements.txt
```

### Running Programm
To start the program, run the following command in a terminal:

```sh 
python3 main.py
```
