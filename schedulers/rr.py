from process import RoundRobin_Process

rr_list = [RoundRobin_Process(exec_time=22),
           RoundRobin_Process(exec_time=2),
           RoundRobin_Process(exec_time=3),
           RoundRobin_Process(exec_time=5),
           RoundRobin_Process(exec_time=8)]


def schedule() -> float:
    print("Round Robin:\n")
    copy_list = rr_list.copy()
    time_counter = 0
    added_timestamps = []
    quantum = 3
    while(len(copy_list) > 0):
        for p in copy_list:
            if(p.exec_time > quantum):
                p.exec_time -= quantum
                time_counter += quantum
            else:
                time_counter += p.exec_time
                print(time_counter, "\n" ) 
                copy_list.remove(p)

    ave_waiting_time = time_counter / len(rr_list)
    print('Average waiting time:', ave_waiting_time)
    return ave_waiting_time
        