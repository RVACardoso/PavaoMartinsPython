
class arvore:

    def __init__(self, *args):
        if args == ():
            self.r = None
        elif len(args) == 3 and isinstance(args[1], arvore) and isinstance(args[2], arvore):
            self.r = args[0]
            self.ar_e = args[1]
            self.ar_d = args[2]
        else:
            raise ValueError("either 0 or 3 arguments")

    def raiz(self):
        if self.r == None:
            raise ValueError("arvore vazia")
        else:
            return self.r

    def arv_esq(self):
        if self.r == None:
            raise ValueError("arvore vazia")
        else:
            return self.ar_e

    def arv_dta(self):
        if self.r == None:
            raise ValueError("arvore vazia")
        else:
            return self.ar_d

    def eh_arv_vazia(self):
        return self.r == None


# A13.1
def numero_noc_arvore(arv):

    if arv.eh_arv_vazia():
        return 0
    else:
        return 1 + numero_noc_arvore(arv.arv_esq()) + numero_noc_arvore(arv.arv_dta())

# A13.2
def prof_maxima_arv(arv):

    if arv.eh_arv_vazia():
        return -1
    else:
        return 1 + max(prof_maxima_arv(arv.arv_esq()), prof_maxima_arv(arv.arv_dta()))

# A13.3
def maior_caminho_arv(in_arv):

    def maior_caminho_aux(path, arv):
        if arv.eh_arv_vazia():
            return path
        else:
            if prof_maxima_arv(arv.arv_esq()) > prof_maxima_arv(arv.arv_dta()):
                if arv.arv_esq().eh_arv_vazia():
                    return path
                else:
                    return maior_caminho_aux(path + [arv.arv_esq().raiz()], arv.arv_esq())
            else:
                if arv.arv_dta().eh_arv_vazia():
                    return path
                else:
                    return maior_caminho_aux(path + [arv.arv_dta().raiz()], arv.arv_dta())

    return maior_caminho_aux([in_arv.raiz()], in_arv)

# A13.4
def numero_folhas_arv(arv):
    # print(arv.raiz())
    if arv.eh_arv_vazia():
        return 0
    elif not arv.eh_arv_vazia() and arv.arv_esq().eh_arv_vazia() and arv.arv_dta().eh_arv_vazia():
        return 1
    else:
        return numero_folhas_arv(arv.arv_esq()) + numero_folhas_arv(arv.arv_dta())

# A13.5
def soma_elementos_arv(arv):
    if arv.eh_arv_vazia():
        return 0
    else:
        return arv.raiz() + soma_elementos_arv(arv.arv_esq()) + soma_elementos_arv(arv.arv_dta())

# A13.6
def espelha_arv(arv):
    if arv.eh_arv_vazia():
        return arv
    else:
        return arvore(arv.raiz(), espelha_arv(arv.arv_dta()), espelha_arv(arv.arv_esq()))


# A13.7
def transform_arv(arv, func):
    if arv.eh_arv_vazia():
        return arv
    else:
        return arvore(func(arv.raiz()), transform_arv(arv.arv_esq(), func), transform_arv(arv.arv_dta(), func))

# A13.9 (with objects)
def procura_prof_arv(arv):
    if arv.eh_arv_vazia():
        return []
    else:
        return [arv.raiz()] + procura_prof_arv(arv.arv_esq()) + procura_prof_arv(arv.arv_dta())

# A13.10 (with objects)
def procura_larg_arv(arv):
    node_lst = [arv]
    visit_order = []
    while len(node_lst) != 0:
        visit_order.append(node_lst[0].raiz())
        if node_lst[0].eh_arv_vazia():
            node_lst += []
        else:
            if not node_lst[0].arv_esq().eh_arv_vazia():
                node_lst.append(node_lst[0].arv_esq())
            if not node_lst[0].arv_dta().eh_arv_vazia():
                node_lst.append(node_lst[0].arv_dta())
        del(node_lst[0])

    return visit_order


# g_1 = arvore()
# g_2 = arvore()
# g = arvore(3, g_1, g_2)
# h_1 = arvore()
# h_2 = arvore()
# h = arvore(4, h_1, h_2)
# e = arvore(5, g, h)
# d_1 = arvore()
# d_2 = arvore()
# d = arvore(6, d_1, d_2)
# f_1 = arvore()
# f_2 = arvore()
# f = arvore(1, f_1, f_2)
# b = arvore(2, d, e)
# c_1 = arvore()
# c = arvore(4, c_1, f)
# a = arvore(9, b, c)


# # g_1 = arvore("I", arvore(), arvore())
# # g_2 = arvore("M", arvore(), arvore())
g_1 = arvore()
g_2 = arvore()
g = arvore("G", g_1, g_2)
h_1 = arvore()
h_2 = arvore()
h = arvore("H", h_1, h_2)
e = arvore("E", g, h)
d_1 = arvore()
d_2 = arvore()
d = arvore("D", d_1, d_2)
f_1 = arvore()
f_2 = arvore()
f = arvore("F", f_1, f_2)
b = arvore("B", d, e)
c_1 = arvore()
c = arvore("C", c_1, f)
a = arvore("A", b, c)

print(procura_larg_arv(a))