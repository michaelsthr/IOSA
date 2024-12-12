from process import Process

edf_list = [Process(deadline=9, exec_time=4),
             Process(deadline=9, exec_time=5),
             Process(deadline=10, exec_time=8)]


def schedule() -> float:
    print('Earliest Deadline First:\n')

    # sorted list only by deadlines, not by execution times
    edf_list.sort(key=lambda process: process.deadline)

    for idx in range(len(edf_list)):
        print('  Execution time process', (idx+1), ':', edf_list[idx].exec_time)


    ave_waiting_time = 0
    added_waiting_time = 0
    rel_waiting_time = 0
    for i in edf_list:
        rel_waiting_time = rel_waiting_time + i.exec_time
        added_waiting_time += rel_waiting_time
        print('+', rel_waiting_time)
        
    print(added_waiting_time, ' / ', len(edf_list))
    ave_waiting_time = added_waiting_time / len(edf_list)
    print('Average waiting time:', ave_waiting_time)
    print('='*40)
    return ave_waiting_time