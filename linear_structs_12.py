
# # 12.1
# def palindromo(word):
#
#     def nova_pilha():
#         return []
#
#     def topo(pilha):
#         return pilha[0]
#
#     def tira(pilha):
#         return pilha[1:]
#
#     def coloca(pilha, elem):
#         return [elem] + pilha
#
#     def eh_pilha_vazia(pilha):
#         return len(pilha)==0
#
#     char_stack = nova_pilha()
#     size = len(word)
#     for elem in word[:size//2]:
#         char_stack = coloca(char_stack, elem)
#     if size % 2 == 0:
#        rest = word[size//2:]
#     else:
#         rest = word[size//2 + 1:]
#
#     for elem in rest:
#         if topo(char_stack) == elem:
#             char_stack = tira(char_stack)
#         else:
#             return False
#     return eh_pilha_vazia(char_stack)
#
# # A12.2
# class fila:
#     def __init__(self):
#         self.f = []
#
#     def inicio(self):
#         if self.f == []:
#             raise ValueError('fila vazia')
#         else:
#             return self.f[0]
#
#     def comprimento(self):
#         return len(self.f)
#
#     def coloca(self, elem):
#         self.f += [elem]
#         return self
#
#     def retira(self):
#         if self.f == []:
#             raise ValueError('fila vazia')
#         else:
#             del(self.f[0])
#
#     def eh_fila_vazia(self):
#         return self.f == []
#
# def soma_fila(fila):
#     sum = 0
#     while not fila.eh_fila_vazia():
#         sum += fila.inicio()
#         fila.retira()
#     return sum
#
# # A12.3
# def nova_fila():
#     return []
#
# def coloca(fila, elem):
#     return fila + [elem]
#
# def retira(fila):
#     return fila[1:]
#
# def inicio(fila):
#     return fila[0]
#
# def eh_fila_vazia(fila):
#     return len(fila)==0

# # A12.4
# class priority_queue:
#     def __init__(self):
#         self.normal = []
#         self.urgent = []
#
#     def inicio_normal(self):
#         if not self.eh_vazia_normal():
#             return self.normal[0]
#         else:
#             raise ValueError("empty ")
#
#     def inicio_urgent(self):
#         if not self.eh_vazia_urgent():
#             return self.urgent[0]
#         else:
#             raise ValueError("empty ")
#
#     def retira_normal(self):
#         del(self.normal[0])
#
#     def retira_urgent(self):
#         del(self.urgent[0])
#
#     def coloca_normal(self, elem):
#         self.normal += [elem]
#
#     def coloca_urgent(self, elem):
#         self.urgent += [elem]
#
#     def eh_vazia_normal(self):
#         return len(self.normal) == 0
#
#     def eh_vazia_urgent(self):
#         return len(self.urgent) == 0
#
#     def inicio(self):
#         if self.eh_vazia_urgent():
#             out = self.inicio_normal()
#             self.retira_normal()
#             return out
#         elif self.eh_vazia_normal():
#             raise ValueError("Filas vazias")
#         else:
#             out = self.inicio_urgent()
#             self.retira_urgent()
#             return out
#
#     def aumenta_prioridade(self):
#         self.coloca_urgent(self.inicio_normal())
#         self.retira_normal()
#
# # A12.5
# class fila_dupla:
#     def __init__(self):
#         self.f = []
#
#     def comprimento(self):
#         return len(self.f)
#
#     def inicio(self):
#         return self.f[0]
#
#     def final(self):
#         return self.f[self.comprimento()-1]
#
#     def coloca_inicio(self, elem):
#         self.f = [elem] + self.f
#
#     def coloca_final(self, elem):
#         self.f = self.f + [elem]
#
#     def retira_inicio(self):
#         del(self.f[0])
#
#     def retira_final(self):
#         del(self.f[self.comprimento()-1])
#
#     def eh_fila_vazia(self):
#         return self.comprimento() == 0

# # A12.6
# class curcular_list:
#     def __init__(self):
#         self.f = []
#
#     def insere_circ(self, elem):
#         self.f = [elem] + self.f
#
#     def primeiro_circ(self):
#         if len(self.f) != 0:
#             return self.f[0]
#         else:
#             raise ValueError("lista vazia")
#
#     def retira_circ(self):
#         if len(self.f) != 0:
#             del(self.f[0])
#         else:
#             raise ValueError("lista vazia")
#
#     def avanca_circ(self):
#         if len(self.f) > 1:
#             self.f += [self.primeiro_circ()]
#             self.retira_circ()
#
#     def el_n_circ(self, n):
#         return self.f[n % len(self.f)]
#
#     def __repr__(self):
#         rep = "@ "
#         for elem in self.f:
#             rep += str(elem) + " "
#         return rep + "@"
