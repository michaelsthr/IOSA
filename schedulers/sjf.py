from process import Process

p1 = Process(name="p1", exec_time=22)
p3 = Process(name="p3", exec_time=3)
p4 = Process(name="p4", exec_time=5)
p2 = Process(name="p2", exec_time=2)
p5 = Process(name="p5", exec_time=8)

processes = [p1, p2, p3, p4, p5]


def schedule():
    print("Shortest Job First:\n")
    
    sorted_list = sorted(processes, key=lambda p: p.exec_time)

    for l in sorted_list:
        print(l)

    # calculate the combined relativ waiting time for each process
    ave_waiting_time = 0
    added_waiting_time = 0
    rel_waiting_time = 0
    for i in sorted_list:
        rel_waiting_time += i.exec_time
        added_waiting_time += rel_waiting_time
        print('+', rel_waiting_time)
        
    # calculate and print the average waiting time
    print(added_waiting_time, ' / ', len(sorted_list))
    ave_waiting_time = added_waiting_time / len(sorted_list)
    print('Average waiting time:', ave_waiting_time)
    print('='*40)
    return ave_waiting_time
