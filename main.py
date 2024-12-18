from schedulers.sjf import ShortestJobFirst

if __name__ == "__main__":
    print("=" * 40)
    print("Welcome to IOSA - Implementation Of Scheduling Algorithms")
    print("Made by: Matthi, Samu, Michi")
    print("=" * 40)
    
    sjf = ShortestJobFirst()
    sjf.schedule()
    sjf.plot()
