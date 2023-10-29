import random
import time
import threading

def random_number(file_name):
    with open(file_name, 'w') as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number))
        time.sleep(1)


start_time = time.time()
for i in range(1000):
    random_number(f'file_{i}.txt')
end_time = time.time()
print(end_time - start_time)


def in_thread(func, args):
    thread = threading.Thread(target=func, args=args)
    thread.start()
    return thread

start_time_multi = time.time()
threads = []
for i in range(1000):
    thread = in_thread(random_number, (f'file_{i}.txt',))
    threads.append(thread)

for thread in threads:
    thread.join()

end_time_multi = time.time()
print(end_time_multi - start_time_multi)