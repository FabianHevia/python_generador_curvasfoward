'''

Construir una curva forward simple dada una lista de tasas spot crecientes.

'''

# Tenemos la siguiente lista de spots
spots = [0.02, 0.025, 0.03, 0.035]
# Creamos la lista de los fowards
forwards = []

for i in range(1, len(spots)):
    # Por cada indice a lo largo de la lista Spots
    # Igualamos la variable s1 y s2 a el indice anterior y el indice actual respectivamente
    s1, s2 = spots[i-1], spots[i]
    # Aplicamos el calculo foward simple
    fwd = ((1+s2)**(i+1) / (1+s1)**i) - 1
    # Añadimos a la lista de fowards el calculo con un redondeo de hasta 5 decimales
    forwards.append(round(fwd, 5))

print(forwards)
