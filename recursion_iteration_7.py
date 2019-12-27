
# # A7.1
# def quadrado_adiado(number):
#
#     def prod(a, b):
#         if b == 1:
#             return a
#         else:
#             return a + prod(a, b-1)
#
#     if number == 1:
#         return 1
#     else:
#         return prod(2, number) - 1 + quadrado_adiado(number-1)
#
# def quadrado_cauda(number):
#     def prod(sum, a, b):
#
#         if b == 1:
#             return sum + a
#         else:
#             return prod(sum+a, a, b-1)
#
#     def quad(sum, count):
#         if count == 1:
#             return sum + 1
#         else:
#             return quad(sum+(2*count-1), count-1)
#
#     return quad(0, number)

# A7.2
# def numero_digitos(number):
#     if number < 10:
#         return 1
#     else:
#         return 1 + numero_digitos(number//10)
#
# def numero_digitos(number):
#
#     def num_digitos_aux(sum, number):
#         if number < 10:
#             return sum + 1
#         else:
#             return num_digitos_aux(sum + 1, number//10)
#
#     return num_digitos_aux(0, number)
#
# def numero_digitos(number):
#     count = 0
#     while number > 9:
#         count += 1
#         number = number//10
#     return count + 1

# A7.3
# def m_p(x, y):
#
#     def m_p_a(prod, x, pot):
#         # print(prod)
#         if pot == 0:
#             return prod
#         else:
#             return m_p_a(prod*x, x, pot-1)
#
#     return m_p_a(1, x, y)

# # A7.5
# def e_capicua(number):
#
#     def capicua_aux(state, number):
#         if number < 10:
#             return state
#         else:
#             end_digit = number % 10
#             start_digit = number // (10**(numero_digitos(number)-1))
#             return capicua_aux(state and (start_digit==end_digit) , (number % (10**(numero_digitos(number)-1)))//10)
#
#     return capicua_aux(True, number)

# # A7.6
# def espelho(number):
#
#     def espelho_aux(res, number):
#         if number < 10:
#             return res*10 + number
#         else:
#             return espelho_aux(res*10 + number%10, number//10)
#
#     return espelho_aux(0, number)

# # A7.8
# def ackermann(m,n):
#     if m==0:
#         return n+1
#     elif m>0 and n==0:
#         return ackermann(m-1,1)
#     elif m > 0 and n > 0:
#         return ackermann(m-1, ackermann(m, n-1))

# # A7.9
# def produto(x, y):
#     if x == 0:
#         return 0
#     elif x % 2 == 0:
#         return produto(x//2, y+y)
#     else:
#         return y + produto(x-1, y) # operacao adiada
#
# def produto(x, y):
#
#     def produto_aux(sum, x, y):
#         if x == 0:
#             return sum
#         elif x % 2 == 0:
#             return produto_aux(sum, x//2, y+y)
#         else:
#             return produto_aux(sum + y, x-1, y)
#
#     return produto_aux(0, x, y)

# # A7.12
# def numero_occ_lista(lst, number):
#
#     def numero_lst_aux(lst):
#         if len(lst) == 0:
#             return 0
#         if isinstance(lst[0], list):
#             return numero_lst_aux(lst[0]) + numero_lst_aux(lst[1:])
#         elif lst[0] == number:
#             return 1 + numero_lst_aux(lst[1:])
#         else:
#             return numero_lst_aux(lst[1:])
#
#     return numero_lst_aux(lst)