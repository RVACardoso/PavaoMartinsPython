
# # A3.3
# def num_divisores(number):
#     iter_val = 1
#     sum = 1
#     while iter_val < number:
#         if number % iter_val == 0:
#             sum += 1
#         iter_val += 1
#     return sum

# A3.4
# def soma_divisores(number):
#     iter_val = 1
#     sum = 0
#     while iter_val <= number:
#         if number % iter_val == 0:
#             sum += iter_val
#         iter_val += 1
#     return sum

# # A3.5
# def primo(number):
#     from math import sqrt, floor
#     sup = floor(sqrt(number))
#     iter_val = 2
#     while iter_val <= sup:
#         if number % iter_val == 0:
#             return False
#         iter_val += 1
#     return number != 0 and number != 1
#
# # A3.6
# def n_esimo_primo(n):
#
#     iter_val = 2
#     count = 0
#     while count < n:
#         if primo(iter_val):
#             count += 1
#         iter_val += 1
#     return iter_val-1

