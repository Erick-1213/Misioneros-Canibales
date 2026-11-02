

inicio= (3, 3, 1)
meta = (0, 0, 0)
acciones= [(1,0), (2, 0), (1, 1), (0, 1), (0,2)] 

def es_valido(estado):
    misioneros, canibales, bote = estado

    mr = 3 - misioneros
    cr = 3 - canibales

    if misioneros < 0 or canibales < 0 or misioneros > 3 or canibales > 3:
        return False
    if misioneros > 0 and canibales > misioneros:
        return False
    if mr > 0 and cr > mr:
        return False
    return True

def generar_sucesores(estado):
    sucesores = []
    misioneros, canibales, bote = estado

    for dm, dc in acciones:

        if bote == 1:
            nuevo_estado = (misioneros - dm, canibales - dc, 0)
        else:  
            nuevo_estado = (misioneros + dm, canibales + dc, 1)

        if es_valido(nuevo_estado):
            sucesores.append(nuevo_estado)
    return sucesores