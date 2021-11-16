import sys
import importlib
from TK_1 import create_new_list
from TK_2 import min_max_value
from TK_3 import list_divided_by_average
from TK_4 import list_multiplied_by_average
TK_5 = importlib.import_module('TK-5')


def main():
    print("Введите размер списка:", end=' ')
    length = int(input())
    new_list = create_new_list(length)
    print("Выполение TK_1: {}".format(new_list))
    print("Выполение TK_2: {}".format(min_max_value(new_list)))
    print("Выполение TK_3: {}".format(list_divided_by_average(new_list)))
    print("Выполение TK_4: {}".format(list_multiplied_by_average(new_list)))
    print("Выполение TK_5: {}".format(TK_5.square_roots_of_numbers(new_list)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
