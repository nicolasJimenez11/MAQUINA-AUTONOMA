import sys

def AFD(cadena):
    e="q1"#estado inicial

    funcionTransicion = {
        ("q1","0"):"q2",
        ("q1","1"):"q3",
        ("q2","0"):"q2",
        ("q2","1"):"q2",
        ("q3","0"):"q3",
        ("q3","1"):"q3"
    }
    F = ["q2"]  # estado final

    if cadena == "":
        return False

    for s in cadena:
        if s != "0" and s != "1":
            return False

        e = funcionTransicion[(e,s)]   # <- TRANSICION DENTRO DEL FOR

    return e in F

archivoTxt = sys.argv[1]

with open(archivoTxt) as archivo:
    lineas = archivo.readlines()

print("resultado")

i = 1
for l in lineas:
    cadena = l.strip()

    if AFD(cadena):
        print("linea", i, ":", cadena, "ACEPTADA")
    else:
        print("linea", i, ":", cadena, "RECHAZADA")

    i += 1