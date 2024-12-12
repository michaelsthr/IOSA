from process import LLF_Process

llf_list = [LLF_Process(ready_time=0, deadline=10, exec_time=8),
            LLF_Process(ready_time=0, deadline=9, exec_time=5), 
            LLF_Process(ready_time=0, deadline=9, exec_time=4)]

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

    sorted_after_lax = sorted(llf_list, key=lambda x: x.laxity, reverse=False)
    print('Least Laxity First:\n')
    print('Processes:')

    for process in llf_list:
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
