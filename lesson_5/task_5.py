import time

if __name__ == '__main__':
    s = time.perf_counter()
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = (i for i in src if src.count(i) == 1)
    print(list(result))
    print(time.perf_counter() - s)
    s = time.perf_counter()
    num_lst = [1, 11, 5, 42, 2, 2, 1]

    unique_nums = set()
    repeat_nums = set()
    for item in num_lst:
        if item not in repeat_nums:
            unique_nums.add(item)
        else:
            unique_nums.discard(item)
            repeat_nums.add(item)

    result = [element for element in num_lst if element in unique_nums]
    print(result)
    print(time.perf_counter() - s)
