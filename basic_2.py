
# # A2.2
# n_segundos = eval(input("escreva o numero de segundos: \n -> "))
# n_dias = n_segundos//(3600*24)
# rmg_segs = n_segundos%(3600*24)
# n_horas = rmg_segs//3600
# rmg_segs = rmg_segs%3600
# n_mins = rmg_segs//60
# n_segs = rmg_segs%60
# print("dias: ", n_dias, "; n_horas: ", n_horas, "; n_mins: ", n_mins, "; n_segs: ", n_segs)

# # A2.3
# numbers = eval(input("escreva numeros separados por virgulas: \n -> "))
# max = numbers[0]
# for i in numbers:
#     if i > max:
#         max = i;
# print("max is: ", max)

# # A2.4
# n_segundos = eval(input("escreva o numero de segundos: \n -> "))
# while n_segundos >= 0:
#     print("nº de dias: ", n_segundos/(3600*24))
#     n_segundos = eval(input("escreva o numero de segundos: \n -> "))

# A2.6
# digito = eval(input("escreva um digito: \n -> "))
# number = 0
# while digito != -1:
#     number = number*10+digito
#     digito = eval(input("escreva um digito: \n -> "))
# print("O numero é: ", number)

# # A2.7
# number = eval(input("escreva um numero: \n -> "))
# sum = 0
# while number > 0:
#     digito = number % 10
#     if digito%2 == 0:
#         sum += digito
#     number = number // 10
# print("soma é: ", sum)

# # A2.8
# number = eval(input("escreva um numero: \n -> "))
# invert = 0
# while number > 0:
#     digito = number % 10
#     number = number // 10
#     invert = invert*10 + digito
# print("numero é", invert)

# # A2.9
# lim = eval(input("escreva o limite: \n -> "))
# sum, iter_val = 0, 0
# while sum < lim:
#     iter_val += 1
#     sum += iter_val
# print("o maior inteiro é: ", iter_val)

# # A2.10
# x = eval(input("escreva x: \n -> "))
# n = eval(input("escreva n: \n -> "))
# res = 1
# term = 1
# for idx in range(n):
#     term *= x/(idx+1)
#     res += term
# print("sum is: ", res)
