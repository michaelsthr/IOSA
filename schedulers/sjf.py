from process import Process

p1 = Process(name="p1", ready_time=40, exec_time=2)
p2 = Process(name="p2", ready_time=2, exec_time=2)
p3 = Process(name="p3", ready_time=5, exec_time=2)
p4 = Process(name="p4", ready_time=10, exec_time=2)
p5 = Process(name="p5", ready_time=8, exec_time=2)

processes = [p1, p2, p3, p4, p5]


def schedule():
    print("Starting sjf\n")
    
    sorted_list = sorted(processes, key=lambda p: p.ready_time)

    for l in sorted_list:
        print(l)
