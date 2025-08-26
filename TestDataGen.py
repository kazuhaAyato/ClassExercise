import random
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
if __name__ == "__main__":
    for i in range(random.randint(10,120)):
        print(random_int_list(random.randint(0,100),random.randint(1000,5000),random.randint(50,4000)))