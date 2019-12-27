
# # A11.1
# class parking:
#
#     # def __init__(self, max_spots):
#     #     self.max_spots = max_spots
#     #     self.taken_spots = 0
#
#     def gets_in(self):
#         if self.taken_spots + 1 <= self.max_spots:
#             self.taken_spots += 1
#         else:
#             print("parque completo")
#
#     def gets_out(self):
#         self.taken_spots -= 1
#
#     def spots(self):
#         free_spots = self.max_spots - self.taken_spots
#         print("free spots: ", free_spots)
#         return free_spots

# # A11.2
# class bottle:
#
#     def __init__(self, max_volume):
#         self.max_volume = max_volume
#         self.curr_volume = 0
#
#     def maximum_volume(self):
#         return self.max_volume
#
#     def current_volume(self):
#         return self.curr_volume
#
#     def dump(self, vol):
#         self.curr_volume -= vol
#         if self.curr_volume < 0:
#             self.curr_volume = 0
#
#     def fill(self, vol):
#         self.curr_volume += vol
#         if self.curr_volume > self.max_volume:
#             self.curr_volume = self.max_volume

# # A11.4
# class instant_time:
#
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def hours(self):
#         return self.hour
#
#     def minutes(self):
#         return self.minute
#
#     def seconds(self):
#         return self.second
#
#     def __repr__(self):
#         return str(self.hours()) + ":" + str(self.minutes()) + ":" + str(self.seconds())
#
#     def __lt__(self, other):
#         t1 = [self.hours(), self.minutes(), self.seconds()]
#         t2 = [other.hours(), other.minutes(), other.seconds()]
#
#         def previous_aux(i):
#             if t1[i] < t2[i]:
#                 return True
#             elif t1[i] > t2[i]:
#                 return False
#             else:
#                 if i == 2:
#                     return False
#                 return previous_aux(i+1)
#
#         return previous_aux(0)
#
#     def __sub__(self, other):
#         if self < other:
#             return None
#         else:
#             return (self.hours()-other.hours())*60 + (self.minutes()-other.minutes()) + round((self.seconds()-other.seconds())/60)

# # A11.6
# class carro:
#     def __init__(self):
#         self.in_time = None
#         self.cost = None
#
#     def set_in_time(self, time):
#         self.in_time = time
#
#     def get_in_time(self):
#         return self.in_time
#
#     def set_cost(self, cost):
#         self.cost = cost
#
#     def get_cost(self):
#         return self.cost
#
#
# class paid_parking(parking):
#
#     def __init__(self, max_spots):
#         self.max_spots = max_spots
#         self.taken_spots = 0
#
#     def gets_in(self, car, time):
#         if self.taken_spots + 1 <= self.max_spots:
#             if isinstance(time, (instant_time)) and car.get_in_time()==None:
#                 self.taken_spots += 1
#                 car.set_in_time(time)
#             else:
#                 raise TypeError("arg time is not instance of class 'instant_time' or car is already inside park.")
#         else:
#             print("parque completo")
#
#     def gets_out(self, car, time):
#         if isinstance(car.get_in_time(), (instant_time)):
#             self.taken_spots -= 1
#             parked_time = time - car.get_in_time()
#             if parked_time < 31:
#                 cost = 0.3
#             elif parked_time < 61:
#                 cost = 0.5
#             else:
#                 cost = 0.8 + 1.5*((parked_time/60)-1)
#             car.set_cost(cost)
#         else:
#             raise TypeError("car is not inside park")


# # A11.7
# class urna:
#     def __init__(self, candidates):
#         self.urna_votes = {}
#         for cand in candidates:
#             self.urna_votes[cand] = 0
#
#     def vote(self, cand):
#         self.urna_votes[cand] += 1
#
#     def __repr__(self):
#         string = ''
#         for cand, votes in self.urna_votes.items():
#             string += "{:5}   {:5} \n".format(cand, votes)
#         return string

# # A11.8
# class pessoa:
#     def __init__(self, nome, nascimento, sexo):
#         self.var_nome = nome
#         self.var_nascimento = nascimento
#         self.var_sexo = sexo
#
#     def nome(self):
#         return self.var_nome
#
#     def nascimento(self):
#         return self.var_nascimento
#
#     def sexo(self):
#         return self.var_sexo
#
#
# class estudante(pessoa):
#     def __init__(self, escola, tipo, *pessoa_data):
#         self.var_escola = escola
#         self.var_tipo = tipo
#         super(estudante, self).__init__(*pessoa_data)
#
#     def escola(self):
#         return self.var_escola
#
#     def tipo_ensino(self):
#         return self.var_tipo
#
#
# class estudante_ist(estudante):
#     def __init__(self, curso, ano_entrada, ano_inscricao, disciplinas):
#         self.var_escola = 'ist'
#         self.var_tipo = 'superior'
#         self.var_curso = curso
#         self.var_ano_entrada = ano_entrada
#         self.var_ano_inscricao = ano_inscricao
#         self.var_disciplinas = disciplinas
#
#     def curso(self):
#         return self.var_curso
#
#     def ano_entrada(self):
#         return self.var_ano_entrada
#
#     def ano(self):
#         return self.var_ano_inscricao
#
#     def disciplinas(self):
#         return self.var_disciplinas
#
#     def curriculum(self):
#         _disciplinas, _melhor_nota = [], []
#         for discip, notas in self.var_disciplinas.items():
#             _disciplinas.append(discip)
#             _melhor_nota.append(max(notas))
#
#         return _disciplinas, _melhor_nota
#
#
# class professor(pessoa):
#     def __init__(self, escola, salario):
#         self.var_escola = escola
#         self.var_salario = salario
#
#     def escola(self):
#         return self.var_escola
#
#     def salario(self):
#         return self.var_salario
#
