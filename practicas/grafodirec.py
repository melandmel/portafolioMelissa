#Este codigo crea un gado dirigido con 4 variables
import matplotlib.pyplot as plt

#Creamos un grafo vacio
grafo = {}

#Agregamos vertices al grafo
grafo["A"] = ["B","C"]
grafo["B"] = ["D"]
grafo["C"] = ["D"]
grafo["D"] = []

#Imprimimos el grafo
print("Grafo")
for vertice, adyacentes in grafo.items():
    print(f"{vertice} -> {adyacentes}")