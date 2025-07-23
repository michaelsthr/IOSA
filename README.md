# IOSA - Implementation Of Scheduling Algorithms
### Developers: Michael Stöhr, Samuel Käufler, Matthias Steger

![IOSA Scheduling Algorithms visualization showing process execution over time](/screenshots/frame.png)

*Screenshot of IOSA visualizing different scheduling algorithms and their impact on process execution.*

### Overview
This project implements various CPU scheduling algorithms in Python. The goal is to provide a clear understanding of how different scheduling strategies work and their impact on process management in operating systems.

### Features
- Interactive command-line interface to select and run different scheduling algorithms.
- Plotting of scheduling results to visualize process execution and waiting times.
- Support for both preemptive and non-preemptive scheduling algorithms.

### Implementations of following algorithms:
- FCFS: First-Come-First-Serve schedules processes in the order they arrive in the ready queue. 
    - It is simple but can lead to the convoy effect.
- SJF non-preemptive: Shortest Job First selects the process with the smallest execution time. 
    - It minimizes average waiting time but requires precise knowledge of execution times.
- SJF preemptive: Similar to the non-preemptive approach, but with the difference, that the running process gets interrupted, when a new process is ready. Now the new shortest-job gets selected again.
- EDF: Earliest Deadline First prioritizes processes with the closest deadlines.
    - It is optimal for real-time systems but can be complex to implement.
- LLF: Least Laxity First schedules processes based on their laxity, which is the difference between their deadline and remaining execution time.
    - It aims to prevent deadline misses.
- Round Robin with Quantum Q: Round Robin assigns a fixed time quantum to each process in a cyclic order. 
    - It ensures fairness but can lead to high context-switching overhead.

### Installation
To install Python, download and install it from [python.org](https://www.python.org/).

To clone the repository, run the following command in your terminal:
```sh
git clone       
```

Create a virtual environment to isolate the project dependencies. You can do this with the following command:
```sh
python3 -m venv venv
``` 

Activate the virtual environment:   
```sh   
source venv/bin/activate
``` 

To install the required dependencies, run the following command:
```sh
pip3 install -r requirements.txt
```

### Running Programm
To start the program, run the following command in a terminal:

```sh 
python3 main.py
```
Now you can type your desired scheduler or example and see the output
