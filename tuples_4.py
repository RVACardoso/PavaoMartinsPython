
# A4.1
# def duplica(tup1):
#     tup2 = ()
#     for elem in tup1:
#         tup2 += (elem, )*2
#     return tup2

# # A4.2
# def explode(number):
#     if not isinstance(number, int):
#         raise TypeError("arg must be type int")
#     tup2 = ()
#     while number > 0:
#         tup2 = (number % 10,) + tup2
#         number = number//10
#     return tup2
#
# # A4.3
# def implode(tup1):
#     if not isinstance(tup1, tuple):
#         raise TypeError("arg must be type tuple")
#     value = 0
#     for elem in tup1:
#         if not isinstance(elem, int) or elem >9 or elem<0:
#             raise TypeError("arg elements must be digits")
#         value = value * 10 + elem
#     return value
#
# # A4.4
# def filtra_pares(tup1):
#     if not isinstance(tup1, tuple):
#         raise TypeError("arg must be type tuple")
#     tup2 = ()
#     for elem in tup1:
#         if not isinstance(elem, int) or elem >9 or elem<0:
#             raise TypeError("arg elements must be digits")
#         if elem % 2 == 0:
#             tup2 += (elem,)
#     return tup2
#
# # A4.5
# def algarismos_pares(number):
#     print(explode(number))
#     print(filtra_pares(explode(number)))
#     return implode(filtra_pares(explode(number)))

# A4.7
# def maior_elemento(tup1):
#     max = -float('Inf')
#     for elem in tup1:
#         if elem > max:
#             max = elem
#     return max

# # A4.8
# def juntos(tup1):
#     count = 0
#     for i in range(len(tup1)-1):
#         if tup1[i] == tup1[i-1]:
#             count += 1
#     return count
#
# # A4.9
# def junta_ordenados(tup1, tup2):
#     len1 = len(tup1)
#     len2 = len(tup2)
#
#     p1, p2 = 0, 0
#     out = ()
#     while True:
#         if p1 == len1:
#             out += tup2[p2:]
#             break
#         if p2 == len2:
#             out += tup1[p1:]
#             break
#
#         if tup1[p1] < tup2[p2]:
#             out += (tup1[p1],)
#             p1 += 1
#         else:
#             out += (tup2[p2],)
#             p2 += 1
#
#     return out

# # A4.13
# def cifra_cesar(message, desloc):
#     import random, math
#     message = tuple(message)
#     out = ()
#     A_ord = ord("A")
#     for elem in message:
#         rand_nr = math.floor( random.uniform(A_ord, ord("Z")) )
#         # print(elem)
#         out += (chr(A_ord + (ord(elem)-A_ord+desloc) % 25), chr(rand_nr))
#         # print(chr(A_ord + (ord(elem)-A_ord+desloc) % 25))
#         # print()
#     return out + (chr(A_ord+desloc),)
#
# def decifra_cesar(message):
#     out = ()
#     A_ord = ord("A")
#     desloc = ord(message[-1])-A_ord
#     message = message[:-1]
#     for i, elem in enumerate(message):
#         if i % 2 == 0:
#             out += (chr(A_ord + (ord(elem)-A_ord-desloc) % 25),)
#     out_str = ""
#     for elem in out:
#         out_str += elem
#     return out_str

