from process import Process

fcfs_list = [Process(exec_time=22),
                Process(exec_time=2), 
                Process(exec_time=3), 
                Process(exec_time=5), 
                Process(exec_time=8)]

def schedule():
    print("Starting fcfs")
