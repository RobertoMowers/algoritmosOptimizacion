INF = float('inf')

def floyd_warshall(graph):
    # Inicializar la matriz de distancias
    dist = [[INF if i != j else 0 for j in range(len(graph))] for i in range(len(graph))]

    # Inicializar la matriz de caminos intermedios
    next_vertex = [[-1 for _ in range(len(graph))] for _ in range(len(graph))]

    # Actualizar la matriz de distancias y de caminos intermedios
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
                next_vertex[i][j] = j

    # Calcular las distancias mínimas y actualizar los caminos intermedios
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex

# Ejemplo de uso
graph = [
    [0, 3, 6, INF],
    [INF, 0, 2, INF],
    [INF, INF, 0, 1],
    [1, INF, INF, 0]
]

distances, next_vertex = floyd_warshall(graph)
print("Matriz de distancias:")
for row in distances:
    print(row)

print("\nMatriz de caminos intermedios:")
for row in next_vertex:
    print(row)