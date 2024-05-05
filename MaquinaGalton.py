import random
import matplotlib.pyplot as plt

def simular_maquina(num_canicas, num_obstaculos):
    resultados = [0] * (num_obstaculos + 1)
    for _ in range (num_canicas):
        posicion = 0
        for _ in range (num_obstaculos):
            direccion = random.choice([-1, 1])
            posicion += direccion
        resultados[posicion] += 1
    return resultados

def graficar_histograma (resultados):
    plt.bar(range(len(resultados)), resultados, color="red")
    plt.xlabel("contenedores")
    plt.ylabel("Cantidad de Canicas")
    plt.title("Histograma de una Maquina de Galton")
    plt.show()
    

if __name__ == "__main__":
    num_canicas = 3000
    num_obstaculos = 12
    resultados = simular_maquina(num_canicas, num_obstaculos)
    graficar_histograma(resultados)
