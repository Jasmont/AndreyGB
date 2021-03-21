if __name__ == '__main__':
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = (i for i in src if src.count(i) == 1)
    print(list(result))
