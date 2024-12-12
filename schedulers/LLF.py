from process import Process

processes = [Process(ready_time=0, deadline=10, exec_time=8),
                Process(ready_time=0, deadline=9, exec_time=5), 
                Process(ready_time=0, deadline=9, exec_time=4)]

def schedule() -> float:
    # The output will be like this:

    # Least Laxity First:

    # Processes:
    # + 22
    # + 24
    # + 27
    # + 32
    # + 40
    # 145  /  5
    # Average waiting time: 29.0


    calc_laxity()
    # sort the list after laxity
    sorted_after_lax = sorted(processes, key=lambda p: p.laxity, reverse=False)
    print('Least Laxity First:\n')
    print('Processes:')

    for process in processes:
        print(process)

    print("After laxity sorted Processes:")

    for process in sorted_after_lax:
        print(process)

     # calculate the combined relativ waiting time for each process
    ave_waiting_time = 0
    added_waiting_time = 0
    rel_waiting_time = 0
    for i in sorted_after_lax:
        rel_waiting_time += i.exec_time
        added_waiting_time += rel_waiting_time
        print('+', rel_waiting_time)
        
    # calculate and print the average waiting time
    print(added_waiting_time, ' / ', len(sorted_after_lax))
    ave_waiting_time = added_waiting_time / len(sorted_after_lax)
    print('Average waiting time:', ave_waiting_time)
    print('='*40)
    return ave_waiting_time

def calc_laxity():
    for idx in range(len(processes)):
        processes[idx].laxity = (processes[idx].deadline - processes[idx].ready_time) - processes[idx].exec_time