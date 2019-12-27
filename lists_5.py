

# # A5.1
# def pertence(number, list):
#     i = 0
#     length = len(list)
#     while i < length:
#         if list[i] == number:
#             return True
#         i += 1
#     return False

# # A5.2
# def substitui(list, velho, novo):
#     for i, elem in enumerate(list):
#         if elem == velho:
#             list[i] = novo

# # A5.4
# def parte(list, number):
#     maior, menor = [], []
#     for elem in list:
#         if elem < number:
#             menor += [elem]
#         else:
#             maior += [elem]
#     return [menor, maior]

# # A5.5
# def inverte(list):
#     list_temp = []
#     for i in range(len(list)-1, -1, -1):
#         list_temp += [list[i]]
#     list[:] = list_temp

# # A5.6
# def remove_repetidos(list):
#     single_list = []
#     for elem in list:
#         if elem not in single_list:
#             single_list += [elem]
#     return single_list

# # A5.7
# def elemento_matriz(matrix, line, col):
#     return matrix[line][col]

# # A5.8
# def print_matrix(matrix):
#     for line_idx, line in enumerate(matrix):
#         line_str = ""
#         for elem_idx, elem in enumerate(line):
#             line_str += "{:3}  "
#         # line_str += "\n"
#         # print(matrix[line_idx])
#         # print(line_str)
#         print(line_str.format(*matrix[line_idx]))


# # A5.9
# def matrix_product(mat1, mat2):
#     if len(mat1[0]) != len(mat2):
#         raise ValueError("matrix dimensions are wrong")
#     res = []
#     for i in range(len(mat1)):
#         line = []
#         for j in range(len(mat2[0])):
#             elem = 0
#             for k in range(len(mat2)):
#                 elem += mat1[i][k] * mat2[k][j]
#             line += [elem]
#         res += [line]
#     return res

# # A5.10
# def euromilhoes():
#     import random
#
#     def gen_random(max, count):
#         out = []
#         while len(out) < count:
#             num = int(random.random() * max) + 1
#             if num not in out:
#                 out += [num]
#         return out
#
#     numeros = sorted(gen_random(50, 5))
#     estrelas = sorted(gen_random(12, 2))
#
#     return [numeros, estrelas]











































# def func(number, list):
#     lim_sup = len(list)-1
#     lim_inf = 0
#
#     while lim_inf < lim_sup:
#         meio = (lim_sup-lim_inf)//2
#         if list[meio] == number:
#             return True
#         elif list[meio] > number:
#             lim_sup = meio - 1
#         else:
#             lim_inf = meio + 1
#
#         print()
#         print(lim_sup)
#         print(lim_inf)
#     return False
#
# print(func(2, (1,2,3,4,5)))
