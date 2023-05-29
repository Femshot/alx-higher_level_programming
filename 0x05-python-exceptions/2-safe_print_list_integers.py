#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count, err_count = 0, 0
    while x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
            x -= 1
        except (ValueError, TypeError):
            count += 1
            x -= 1
            err_count += 1
    print("{}".format(''))
    return (count - err_count)
