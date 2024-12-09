from process import Process

edf_list = [Process(deadline=9, exec_time=4),
             Process(deadline=9, exec_time=5),
             Process(deadline=10, exec_time=8)]

def Schedule() -> float:
    print("Earliest deadline first!\n")
    print('Processes:\nExecution-Times:')

    for idx in range(len(edf_list)):
        print('  Execution time process', (idx+1), ':', edf_list[idx].exec_time)
    
    added_exe_time = 0
    is_even_processes = (len(edf_list)/2 == 0)
    for i in edf_list:
        # if ((i == edf_list[0]) or (i == edf_list[1])):
        #     added_exe_time += i.exec_time
        # if (i == edf_list[-1]):
        #     avg_waiting_time = added_exe_time / len(edf_list)
        if is_even_processes:
            if (i != edf_list[-2]):
                added_exe_time += i.exec_time
            else:
                avg_waiting_time = added_exe_time / len(edf_list)
                return avg_waiting_time
        else:
            if (i != edf_list[-1]):
                added_exe_time += i.exec_time
            else:
                avg_waiting_time = added_exe_time / len(edf_list)
                return avg_waiting_time