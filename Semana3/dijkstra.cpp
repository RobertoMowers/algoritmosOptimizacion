#include <iostream>
#include <vector>
#include <utility> // Para std::pair
using namespace std;

class Grafo {
private:
    int V; // Número de vértices
    vector<vector<pair<int, int>>> ady; // Lista de adyacencia: {destino, peso}

public:
    // Constructor
    Grafo(int vertices) {
        V = vertices;
        ady.resize(V);
    }

    // Función para agregar una arista al grafo dirigido con peso
    void agregarArista(int origen, int destino, int peso) {
        ady[origen].push_back({destino, peso});
    }

    // Función para imprimir el grafo
    void imprimirGrafo() {
        for (int i = 0; i < V; ++i) {
            cout << "Nodo " << i << " :";
            for (auto& vecino : ady[i]) {
                cout << " -> " << vecino.first << " (Peso: " << vecino.second << ")";
            }
            cout << endl;
        }
    }
};


int main() {
    Grafo grafo(10); // Por ejemplo, un grafo con 10 nodos

    // Agregar algunas aristas con pesos
    grafo.agregarArista(0, 1, 2);
    grafo.agregarArista(0, 2, 5);
    grafo.agregarArista(1, 3, 3);
    grafo.agregarArista(1, 5, 2);
    grafo.agregarArista(2, 4, 7);
    grafo.agregarArista(3, 4, 2);
    grafo.agregarArista(3, 5, 6);
    grafo.agregarArista(4, 6, 2);
    grafo.agregarArista(4, 7, 5);
    grafo.agregarArista(5, 9, 5);
    grafo.agregarArista(6, 9, 3);
    grafo.agregarArista(7, 8, 4);
    grafo.agregarArista(8, 9, 1);
    

    // Imprimir el grafo
    cout << "Representación del grafo:" << endl;
    grafo.imprimirGrafo();

    return 0;
}
