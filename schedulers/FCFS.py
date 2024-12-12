from process import Process

processes = [Process(exec_time=22),
                Process(exec_time=2), 
                Process(exec_time=3), 
                Process(exec_time=5), 
                Process(exec_time=8)]

def schedule() -> float:
    # The output will be like this:

    # First Come First Serve:

    # Processes:
    # Execution-Times:
    # Execution time process 1 : 22
    # Execution time process 2 : 2
    # Execution time process 3 : 3
    # Execution time process 4 : 5
    # Execution time process 5 : 8
    # + 22
    # + 24
    # + 27
    # + 32
    # + 40
    # 145  /  5
    # Average waiting time: 29.0


    print('First Come First Serve:\n')
    print('Processes:\nExecution-Times:')

    # print the details of the input processes
    for idx in range(len(processes)):
        print('  Execution time process', (idx+1), ':', processes[idx].exec_time)

    # calculate the combined relativ waiting time for each process
    ave_waiting_time = 0
    added_waiting_time = 0
    rel_waiting_time = 0
    for i in processes:
        rel_waiting_time += i.exec_time
        added_waiting_time += rel_waiting_time
        print('+', rel_waiting_time)
        
    # calculate and print the average waiting time
    print(added_waiting_time, ' / ', len(processes))
    ave_waiting_time = added_waiting_time / len(processes)
    print('Average waiting time:', ave_waiting_time)
    print('='*40)
    return ave_waiting_time



