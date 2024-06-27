import numpy as np
import matplotlib.pyplot as plt

def rastrigin(x,y):
    return 20 + x**2 + y**2 - 10*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y))

def graficar_ciudades(cities, title="Ciudades",mejor_punto=0):
    fig, ax = plt.subplots()
    
    plt.ylim(min([city[1] for city in cities])-10, max([city[1] for city in cities])+10)
    plt.xlim(min([city[0] for city in cities])-10, max([city[0] for city in cities])+10)
    ax.scatter(
        [city[0] for city in cities],
        [city[1] for city in cities],
    )
    ax.scatter(cities[mejor_punto][0], cities[mejor_punto][1], color='red', label='Mejor Punto global')
    plt.legend()

    for i in range(len(cities)):
        ax.annotate(f'{i+1}', (cities[i][0], cities[i][1]), fontsize=12, color='black')

    plt.axis("auto")
    plt.title(title)

    plt.savefig(f"./img/{title}.png")
    plt.close()

def calcular_velocidad(velocidad_antigua, posicion_antigua, mejor_posicion_particula, mejor_posicion_global):
    componente_local = mejor_posicion_particula - posicion_antigua
    componente_global = mejor_posicion_global - posicion_antigua
    return velocidad_antigua + 0.5 * componente_local + 0.5 * componente_global 

def calcular_posicion(posicion_antigua, velocidad):
    return posicion_antigua + velocidad

def main():
    
    mejores = [[0, 0], [0, 0], [0, 0], [0, 0]]
    # Definir las posiciones iniciales de las particulas
    p1 = np.array([0, 4])
    v1 = np.array([0, 2.5])
    mejores[0] = p1

    p2 = np.array([10, 0])
    v2 = np.array([2.5, 0])
    mejores[1] = p2
    
    p3 = np.array([0, -4])
    v3 = np.array([0, 2.5])
    mejores[2] = p3
    
    p4 = np.array([-10, 0])    
    v4 = np.array([2.5, 0])
    mejores[3] = p4
    posiciones = [p1, p2, p3, p4]
    velocidades = [v1, v2, v3, v4]
    mejor_global = mejores[1]
    mejor_particula = 1

    for i in range(10):
        print(f"Iteracion {i+1}")
        print("--------------------")
        for particula in range(4):
            print(f"Particula {particula+1}")
            v = calcular_velocidad(velocidades[particula], posiciones[particula], mejores[particula], mejor_global)
            velocidades[particula] = v
            p = calcular_posicion(posiciones[particula], v)
            posiciones[particula] = p
            if rastrigin(p[0], p[1]) > rastrigin(mejores[particula][0], mejores[particula][1]):
                mejores[particula] = p
            print(f"Velocidad: {v}")
            print(f"Posicion: {p}")
            print(f"Mejor posicion: {mejores[particula]}, valor = {rastrigin(mejores[particula][0],mejores[particula][1])}\n")
        for particula in range(4):
            if rastrigin(mejores[particula][0], mejores[particula][1]) > rastrigin(mejor_global[0], mejor_global[1]):
                mejor_global = mejores[particula]
                mejor_particula = particula
        print(f"Mejor global: {mejor_global}, valor = {rastrigin(mejor_global[0],mejor_global[1])}, mejor particula = {mejor_particula+1}\n\n")
        graficar_ciudades(posiciones, f"iteracion_{i+1}",mejor_particula)


if __name__ == "__main__":
    main()