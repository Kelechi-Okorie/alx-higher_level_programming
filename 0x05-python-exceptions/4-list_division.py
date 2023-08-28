#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_len):
    result = []

    for i in range(0, list_len):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except IndexError:
            ans = 0
            print("out of range")
        except TypeError:
            ans = 0
            print("wrong type")
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        finally:
            result.append(ans)

    return result
