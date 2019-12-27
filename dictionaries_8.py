
# # A8.2
# def baralho():
#     valor_list = ['A'] + list(range(2,11)) + ['J', 'Q','K']
#     cartas = []
#     for naipe in ['esp', 'copas', 'ouros', 'paus']:
#         for valor in valor_list:
#             cartas += [{'np':naipe, 'val':valor}]
#     return cartas
#
# def baralha(lst):
#     import random
#     size = len(lst)
#     for carta1 in range(size):
#         carta2 = int(random.random() * size)
#         lst[carta1], lst[carta2] = lst[carta2], lst[carta1]

# # A8.3
# def conta_palavras(sentence):
#
#     words_dict = {}
#     word = ''
#     sentence += ' '
#     for elem in sentence:
#         if elem == ' ':
#             if word != '':
#                 if word in words_dict:
#                     words_dict[word] += 1
#                 else:
#                     words_dict[word] = 1
#             word = ''
#         else:
#             word += elem
#
#     return words_dict

# # A8.4
# def mostra_ordenado(dict1):
#
#     _keys, _vals = [], []
#     for key, val in dict1.items():
#         _keys += [key]
#         _vals += [val]
#
#     change = True
#     while change:
#         change = False
#         for i in range(len(dict1)-1):
#             if _vals[i] < _vals[i+1]:
#                 _vals[i], _vals[i+1] = _vals[i+1], _vals[i]
#                 _keys[i], _keys[i+1] = _keys[i+1], _keys[i]
#                 change = True
#
#     for i in range(len(dict1)):
#         print("{:7}   {:2}".format(_keys[i], _vals[i]))

# # A8.8
# def junta(d1, d2):
#
#     def get_full_keys():
#         _keys_tot = list(d1.keys())
#         _keys2 = list(d2.keys())
#         for key in _keys2:
#             if key not in _keys_tot:
#                 _keys_tot += [key]
#         return _keys_tot
#
#     _keys_tot = get_full_keys()
#
#     d3 = {}
#     for key in _keys_tot:
#         try:
#             d3[key] = d1[key] + d2[key]
#         except KeyError:
#             try:
#                 d3[key] = d1[key]
#             except KeyError:
#                 d3[key] = d2[key]
#     return d3
#
# d1 = {'g':[12,1], 'z':[5], 'a':[98,32]}
# d2 = {'f':[3], 'g':[33,44], 'a':[-8]}
# print(junta(d1, d2))

# # A8.9
# def escreve_esparsa(n, m, dict1):
#     matrix = []
#     for i in range(n):
#         matrix += [[]]
#         for j in range(m):
#             matrix[i] += [0]
#             try:
#                 matrix[i][j] = dict1[(i+1, j+1)]
#             except KeyError:
#                 pass
#     return matrix
#
# def soma_esparsa(n, m, dict_list):
#     matrix = []
#     for i in range(n):
#         matrix += [[]]
#         for j in range(m):
#             matrix[i] += [0]
#
#     for dict in dict_list:
#         for key in dict:
#             matrix[key[0]-1][key[1]-1] += dict[key]
#
#     return matrix

# # A8.10
# def inverte_dic(dict1):
#
#     new_keys = []
#     for vals in dict1.values():
#         for elem in vals:
#             if elem not in new_keys:
#                 new_keys += [elem]
#     # print(new_keys)
#
#     new_dict = {}
#     for key in new_keys:
#         for init_key, init_vals in dict1.items():
#             for elem in init_vals:
#                 if elem == key:
#                     try:
#                         new_dict[key] += [init_key]
#                     except KeyError:
#                         new_dict[key] = [init_key]
#     return new_dict

# # A8.12
# tab1 = {(1,'H'):('branca', 'torre'), (2,'F'): ('branca', 'peao'),
#         (2,'G'): ('branca','rei'), (6,'F'): ('branca','bispo'),
#         (5,'C'): ('branca','rainha'), (6,'G'): ('preta','peao'),
#         (7,'F'): ('preta','peao'), (8,'F'): ('preta','torre'),
#         (8,'G'): ('preta','rei'), (2,'C'): ('preta','peao') }

# def ataques_rainha(tabul):
#
#     atacks = []
#     for rainha_pos, rainha_piece in tabul.items():
#         if rainha_piece[1] == 'rainha':
#             for pos, piece in tabul.items():
#                 if piece[0] != rainha_piece[0]:
#                     if pos[0] == rainha_pos[0]:
#                         atacks += [[piece, pos]]
#                     elif pos[1] == rainha_pos[1]:
#                         atacks += [[piece, pos]]
#                     elif abs(ord(pos[1]) - ord(rainha_pos[1])) == abs(pos[0] - rainha_pos[0]):
#                         atacks += [[piece, pos]]
#     return atacks

# A8.13
# def move_cavalo(cav_pos):
#     final_pos = []
#     for var1 in [-2, +2]:
#         for var2 in [-1, +1]:
#                 final_pos += [[cav_pos[0] + var1, chr(ord(cav_pos[1]) + var2)]]
#                 final_pos += [[cav_pos[0] + var2, chr(ord(cav_pos[1]) + var1)]]
#
#     return final_pos
