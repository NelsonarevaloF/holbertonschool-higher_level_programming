#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    resultado = 0
    for iterator in range(list_length):
        try:
            resultado = my_list_1[iterator] / my_list_2[iterator]
        except ZeroDivisionError:
            resultado = 0
            print("division by 0")
        except (ValueError, TypeError):
            resultado = 0
            print("wrong type")
        except IndexError:
            resultado = 0
            print("out of range")
        finally:
            new_list.append(resultado)
    return new_list
