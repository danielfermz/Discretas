# Proyecto final Matematicas Discretas 
La intencion de este proyecto es expandir y derivar una funcion dada por el usuario.
Se utiliza la libraria Sympy como recruso para la expansion y hallar la expresion derivada y utilizando la aproximacion por definicion y sustituyendo el valor en la expresion derivada

# Manual de usuario 

Requisitos
Para poder ejecutar el script, necesitas tener instalado lo siguiente:
Python 3.x
Las librerías SymPy y NumPy

Al ejecutar el script, lo primero que verás es una solicitud para que escribas tu función:
--- 1. Operaciones Simbólicas (Expandir y Derivar) ---
Introduce la función en términos de x (ej. (x+1)**2):
Escribe tu función y presiona Enter. Debes usar la sintaxis de Python:
Potencias: x**3 (para x^3)
Multiplicación: 5*x (para 5x)
Funciones trigonométricas, exponenciales, etc.: sin(x), cos(x), exp(x).

Inmediatamente, el programa mostrará en pantalla la función original, su forma expandida y la fórmula de su derivada.

Etapa 2: Evaluación en un Punto

A continuación, el programa te pedirá que ingreses un valor numérico:

--- 2. Evaluación de la Derivada en un Punto ---
Introduce el valor de x donde quieres evaluar la derivada:
Escribe el número (puede ser entero o decimal) en el que deseas conocer el valor de la derivada y presiona Enter.

El programa te devolverá dos valores para que los compares:

El resultado numérico, calculado con la aproximación a la definición de la derivada.

El resultado exacto, obtenido al evaluar el punto en la fórmula simbólica.

# Manejo de Errores
Si la función que introduces tiene un error de sintaxis (por ejemplo, escribes x^2 en lugar de x**2, o 2x en lugar de 2*x), el programa lo detectará, mostrará un mensaje de error y se detendrá
