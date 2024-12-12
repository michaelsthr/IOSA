from process import Process

llf_list = [Process(ready_time=0, deadline=10, exec_time=8),
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
    print('Least Laxity First:\n')
    print('Processes:\n')

    # print the details of the input processes
    # for idx in range(len(llf_list)):
    #     print('Process', idx, ':', llf_list[idx].print_all())

def calc_laxity():
    for idx in range(len(llf_list)):
        llf_list[idx].laxity = (llf_list[idx].deadline - llf_list[idx].ready_time) - llf_list[idx].exec_time