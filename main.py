import time

from timer import Timer

def main():
    # Instantiate Timer
    t1 = Timer("Workout",45) #in min
    t2 = Timer("Meditation", 10) #in min
    print("Running timer simulation for 1 second...")
    time.sleep(1)

    t1._paused = False
    print(f"Paused: {t1._paused}")
    del t1._paused
    timers = [t1, t2]
    print(timers)  #  use __repr

    # use clone eval(repr(t))
    clone = eval(repr(t1))
    print("Clone created:", clone)

if __name__ == "__main__":
    main()




# eval playground
# eval("print('hello, running via eval')")

# command = input('enter command:')
# while command != 'exit':
#     eval(command)
#     command = input('enter command:')