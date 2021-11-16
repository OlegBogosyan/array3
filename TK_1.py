def create_new_list(length):
    new_list = []
    for i in range(length):
        print("Введите {0} элемент:".format(i), end=' ')
        new_list.append(int(input()))

    return new_list
