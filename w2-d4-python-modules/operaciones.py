from calculo import multiplica

def rescaler(valores,pesos):
    return sum([multiplica(a,b) for a,b in zip(valores,pesos)])