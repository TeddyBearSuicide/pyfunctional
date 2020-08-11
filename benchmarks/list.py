import time

from pyfunctional import List


def filter_benchmark():
    test_list = List(range(10_000_000))

    start = time.time_ns()
    test_list.filter(lambda x: x % 2 == 0)
    end = time.time_ns()

    print(f"C Filter: {(end - start) / 1e9}")

    start = time.time_ns()
    test_list.filter(lambda x: x % 2 == 0)
    end = time.time_ns()

    print(f"List filter: {(end - start) / 1e9}")


def map_benchmark():
    test_list = List(range(10_000_000))

    start = time.time_ns()
    list(map(lambda x: x * 2, test_list))
    end = time.time_ns()

    print(f"Map: {(end - start) / 1e9}")

    start = time.process_time_ns()
    test_list.map(lambda x: x * 2)
    end = time.process_time_ns()

    print(f"List map: {(end - start) / 1e9}")


def len_benchmark(number=1):
    test_list = [i for i in range(1_000_000)]

    iteration = range(number)

    start = time.time_ns()
    for i in iteration:
        len(test_list) == 0
    end = time.time_ns()

    print(f"Len: {(end - start) / 1e9}")

    start = time.process_time_ns()
    for i in iteration:
        any(test_list)
    end = time.process_time_ns()

    print(f"Any: {(end - start) / 1e9}")


if __name__ == '__main__':
    len_benchmark(1_000_000)

