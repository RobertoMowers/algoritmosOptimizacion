#include <iostream>
#include <cmath>
using namespace std;

// Definir la función f(x) y su derivada f'(x)
double funcion(double x) {
    return x * x - 2;  // Escribe tu función aquí
}

double derivada(double x) {
    return 2 * x;  // Escribe la derivada de tu función aquí
}

// Método de Newton-Raphson
double newtonRaphson(double estimacionInicial, double tolerancia, int maxIteraciones) {
    double x = estimacionInicial;
    
    for (int i = 0; i < maxIteraciones; ++i) {
        double fx = funcion(x);
        double fpx = derivada(x);
        
        // Evitar la división por cero
        if (std::abs(fpx) < 1e-6) {
            std::cerr << "La derivada es cercana a cero. El método no converge." << std::endl;
            return std::numeric_limits<double>::quiet_NaN();
        }

        // Actualizar la estimación
        x = x - fx / fpx;

        // Verificar la convergencia
        if (std::abs(fx) < tolerancia) {
            std::cout << "Convergencia alcanzada en la iteración " << i + 1 << std::endl;
            return x;
        }
    }

    std::cerr << "El método no converge después de " << maxIteraciones << " iteraciones." << std::endl;
    return std::numeric_limits<double>::quiet_NaN();
}

int main() {
    double estimacionInicial;
    cout << "Introducir estimacion Inicial: \n";
    cin >> estimacionInicial;  // Estimación inicial
    double tolerancia = 1e-6;        // Criterio de convergencia
    int maxIteraciones;        // Número máximo de iteraciones
    cout << "Introducir maximo de Iteraciones: \n";
    cin >> maxIteraciones;

    double resultado = newtonRaphson(estimacionInicial, tolerancia, maxIteraciones);

    if (!std::isnan(resultado)) {
        std::cout << "La raíz aproximada es: " << resultado << std::endl;
    }

    return 0;
}
