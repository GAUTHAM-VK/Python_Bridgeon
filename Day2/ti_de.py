import time
def timmer(func):
    def wrapper():
        
        start_time=time.time()
        func()
        end_time=time.time()
        print(f"Execution time:{end_time-start_time}")
        return wrapper
@timmer
def count_numbers():
    for i in range(1000000):
        pass