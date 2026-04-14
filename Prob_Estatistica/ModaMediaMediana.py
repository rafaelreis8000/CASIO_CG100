def calcular_moda(v):
    c = {}
    for i in v:
        if i == v:
            c[i] += 1
        else:
            c[i] = 1
    
    moda = max(c.values())

    modas = []
    for valor, freq in c.items():
        if freq == moda:
            modas.append(v)
    
    return modas
    

def calcular_mediana(v):
    pass

def calcular_media(v):
    
    calc = sum(v)/len(v)
    return calc

valores = [1, 2, 2, 2, 5, 7, 6, 8]
#calcular_media(valores)
calcular_moda(valores)