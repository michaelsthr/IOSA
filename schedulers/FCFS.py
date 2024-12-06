from process import Process

fcfs_list = [Process(exec_time=22),
                Process(exec_time=2), 
                Process(exec_time=3), 
                Process(exec_time=5), 
                Process(exec_time=8)]

def schedule() -> float:
    print('First Come First Serf:\n')
    print('Processes:\nExecution-Times:')

    for idx in range(len(fcfs_list)):
        print('  Execution time process', (idx+1), ':', fcfs_list[idx].exec_time)


    ave_waiting_time = 0
    added_waiting_time = 0
    rel_waiting_time = 0
    for i in fcfs_list:
        rel_waiting_time = rel_waiting_time + i.exec_time
        added_waiting_time += rel_waiting_time
        print('+', rel_waiting_time)
        
    print(added_waiting_time, ' / ', len(fcfs_list))
    ave_waiting_time = added_waiting_time / len(fcfs_list)
    print('Average waiting time:', ave_waiting_time)
    print('='*40)
    return ave_waiting_time



