#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void encontrarSumaCero(vector<int>& arreglo, int size);

int main() {
    vector<int> arreglo;
    int nums;
    int valor;
    int size;

    cout << "Ingrese la cantidad de numeros que tendra el arreglo: ";
    cin >> nums;

    cout << "Ingresar los valores del arreglo:\n";  

    for (int i = 0; i < nums; i++) {
        cout << "Ingrese el valor " << i + 1 << ": ";
        cin >> valor;
        arreglo.push_back(valor);
    }

    cout << "Ingresar el tamano de los subconjuntos:\n";  

    cin >> size;

    sort(arreglo.begin(), arreglo.end());

    for (int i = 0; i < arreglo.size(); i++) {
        cout << arreglo[i] << " ";
    }
    cout << "\n";

    int posicion = 0;

    encontrarSumaCero(arreglo,size);

    return 0;
}

void encontrarSumaCero(vector<int>& arreglo, int size) {
    
}
