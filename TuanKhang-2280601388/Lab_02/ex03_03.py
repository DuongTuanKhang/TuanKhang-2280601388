def tao_tuple_list(lst):
    return tuple(lst)
input_list = input("Nhập một dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
