from collections import deque

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
            sucesores.append((nuevo_estado, (dm, dc)))
    return sucesores

def busqueda_bfs(inicio, meta):
    frontera = deque([inicio])
    visitados = set([inicio])
    padres = {inicio: None}  
    nodos_expandidos = 0

    while frontera:
        nodo_actual = frontera.popleft()
        nodos_expandidos += 1

        if nodo_actual == meta:
            camino = []
            rastreador = meta
            while rastreador is not None:
                camino.append(rastreador)
                rastreador = padres[rastreador]
            return camino[::-1], nodos_expandidos

        for sucesor, accion in generar_sucesores(nodo_actual):
            if sucesor not in visitados:
                visitados.add(sucesor)
                frontera.append(sucesor)
                padres[sucesor] = nodo_actual

    return None, nodos_expandidos