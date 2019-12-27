
# # A9.1
# def create_vector(x, y):
#     return (x, y)
#
# def abcissa(vec):
#     return vec[0]
#
# def ordenada(vec):
#     return vec[1]
#
# def eh_vector(vec):
#     return isinstance(vec, (tuple)) and len(vec)==2 and isinstance(vec[0], (float, int)) and isinstance(vec[1], (float, int))
#
# def eh_vector_nulo(vec):
#     return abs(abcissa(vec))<0.0001 and abs(ordenada(vec))<0.0001
#
# def vectores_iguais(vec1, vec2):
#     return abs(abcissa(vec1)-abcissa(vec2)) < 0.0001 and abs(ordenada(vec1)-ordenada(vec2)) < 0.0001

# # A9.2
# def add_vectors(v1, v2):
#     return create_vector(abcissa(v1)+abcissa(v2), ordenada(v1)+ordenada(v2))
#
# def dot_product(v1, v2):
#     return abcissa(v1)*abcissa(v2) + ordenada(v1)*ordenada(v2)
#
# def colinear_x(v1):
#     return ordenada(v1) == 0

# A9.5
# def create_date(d, m, a):
#     return {'d': d, 'm': m, 'a': a}
#
# def get_day(date):
#     return date['d']
#
# def get_month(date):
#     return date['m']
#
# def get_year(date):
#     return date['a']
#
# def is_date(date):
#     return isinstance(date, (dict)) and len(date)==3 and 'd' in date and 'm' in date and 'a' in date and \
#            isinstance(get_day(date), (int)) and isinstance(get_day(date), (int)) and isinstance(get_day(date), (int))
#
# def equal_dates(dat1, dat2):
#     return get_day(dat1) == get_day(dat2) and get_month(dat1) == get_month(dat2) and get_year(dat1) == get_year(dat2)
#
# def write_date(dat1):
#     if get_day(dat1) < 10:
#         day = '0' + str(get_day(dat1))
#     else:
#         day = str(get_day(dat1))
#     if get_day(dat1) < 10:
#         month = '0' + str(get_month(dat1))
#     else:
#         month = str(get_month(dat1))
#     if get_year(dat1) < 1000:
#         date_year = get_year(dat1)
#         year = ""
#         for _ in range(5-len(str(date_year))):
#             year += '0'
#         if date_year < 0:
#             year = '-' + year + str(abs(date_year))
#         else:
#             year += str(abs(date_year))
#
#     if get_year(dat1) < 0:
#         print(day, "/", month, "/", year, " AC")
#     else:
#         print(day, "/", month, "/", year)
#
# def previous_date(dat1, dat2):
#
#     d1 = [get_day(dat1), get_month(dat1), get_year(dat1)]
#     d2 = [get_day(dat2), get_month(dat2), get_year(dat2)]
#
#     def check_date(n):
#         if d1[n] < d2[n]:
#             return True
#         elif d1[n] > d2[n]:
#             return False
#         else:
#             if n == 0:
#                 return False
#             return check_date(n-1)
#
#     return check_date(2)

# # A9.10
# def create_stack():
#     return []
#
# def push_stack(stk, elem):
#     stk += [elem]
#
# def top(stk):
#     return stk[len(stk)-1]
#
# def remove(stk):
#     del stk[len(stk)-1]
#
# def is_stack(stk):
#     return isinstance(stk, (list))
#
# def is_empty_stack(stk):
#     return len(stk)==0
