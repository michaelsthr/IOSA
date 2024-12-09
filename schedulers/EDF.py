from process import Process

edf_list = [Process(deadline=9, exec_time=4),
             Process(deadline=9, exec_time=5),
             Process(deadline=10, exec_time=8)]

def Schedule() -> float:
    print("Earliest deadline first!\n")
    print('Processes:\nExecution-Times:')

    for idx in range(len(edf_list)):
        print('  Execution time process', (idx+1), ':', edf_list[idx].exec_time)
    
    exe_time = 0
    added_waiting_time = 0

    for i in edf_list:
        if ((i == edf_list[0]) or (i == edf_list[1])):
            exe_time += i.exec_time
        if (i == edf_list[-1]):
            avg_waiting_time = added_waiting_time / len(edf_list)

    return avg_waiting_time