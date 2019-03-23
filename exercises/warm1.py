# def transformar_cadena(cadena):
# 	# Que deberia hacer para construir una cadena revertida?
#
#     for caracter in cadena:
#
#
#
#     #print(cadena.reverse())
# pass
#
# mi_nombre = "mario"
# transformar_cadena(mi_nombre)


def transform(str_f):
    response = ""
    for i in reversed(str_f):
        response += i
    return response


str_f = "ludovico"
print(transform(str_f))



# nombre = "Mario"
# lista = list(nombre)
# lista.reverse()
# nueva = "".join(lista)
# print(nueva)
