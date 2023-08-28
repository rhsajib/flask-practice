
import time


def my_dec(func):
    def do():
        tick = time.time()
        
        tock = time.time()
        print('\nRun time ', tock-tick )
    return do



def runtime(func):
    def do():
        tick = time.time()
        func()
        tock = time.time()
        print('\nRun time ', tock-tick )
    return do


@runtime
def main():
    for i in range(10):
        print(i, end=' => ')


if __name__ == '__main__':
    main()