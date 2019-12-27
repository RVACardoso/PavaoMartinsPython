
# # A6.1
# def soma_digitos_pares(number):
#     if number == 0:
#         return 0
#     elif (number % 10)%2 == 0:
#         return number % 10 + soma_digitos_pares(number//10)
#     else:
#         return soma_digitos_pares(number//10)

# # A6.2
# def inverte_digitos(number):
#
#     def num_digitos(num):
#         if num < 10:
#             return 1
#         else:
#             return 1 + num_digitos(num//10)
#
#     # print(str(number))
#     if number == 0:
#         return 0
#     else:
#         return (number % 10)*10**(num_digitos(number)-1) + inverte_digitos(number//10)

# # A6.4
# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     else:
#         init_num = lst[0]
#         menor, maior = [], []
#         for elem in lst:
#             if elem < init_num:
#                 menor += [elem]
#             elif elem > init_num:
#                 maior += [elem]
#         return quick_sort(menor) + [init_num] + quick_sort(maior)

# # A6.5
# def transforma(tr, lst):
#     if len(lst) == 1:
#         return [tr(*lst)]
#     else:
#         return [tr(lst[0])] + transforma(tr, lst[1:])
#
#
# def filtra(teste, lst):
#     if len(lst) == 0:
#         return []
#     if teste(lst[0]):
#         if len(lst) == 1:
#             return [lst[0]]
#         else:
#             return [lst[0]] + filtra(teste, lst[1:])
#     else:
#         return filtra(teste, lst[1:])

# # A6.6
# def soma_quadrados_lista(lst):
#     def transform(func, lst):
#         out = []
#         for elem in lst:
#             out = out + [func(elem)]
#         return out
#
#     return transform(lambda x: x*x, lst)

# # A6.8
# def sin(x, count):
#
#     def piatorio(a, b, fn, prox):
#         res = 1
#         while a <= b:
#             res *= fn(a)
#             a = prox(a)
#         return res
#
#     return x*piatorio(1, count, lambda a: (1-( x / (a*3.141592))**2), lambda a: a+1)

# A6.9
# def faz_potencia(n):
#
#     def potencia(x):
#         m = n
#         pot = 1
#         while m > 0:
#             pot *= x
#             m = m - 1
#         return pot
#         # return x ** n
#     return potencia

# # A6.10
# def h(f,g):
#     def func(x):
#         return f(x)*f(x)+4*g(x)**3
#     return func
#
# # A6.11
# def derivada_n(f, n):
#     delta = 1e-5
#     def derivada(x):
#         return (f(x+delta)-f(x))/delta
#
#     if n == 0:
#         return f
#     else:
#         return derivada_n( derivada, n-1)

# # A6.14
# def rasto(name, f):
#
#     def func(x):
#         print("Avaliacao de ", name, " com argumento ", x)
#         res = f(x)
#         print("Resultado ", res)
#         return res
#
#     return func
