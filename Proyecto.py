import sympy as sp

def operaciones_simbolicas():
    """
    Pide al usuario una función, la expande, calcula su derivada simbólica y
    muestra los resultados.
    """
    print("--- 1. Operaciones Simbólicas (Expandir y Derivar) ---")
    
    # Pide al usuario que ingrese la función como un texto
    expresion_str = input("Introduce la función en términos de x (ej. (x+1)**2): ")
    x = sp.symbols('x') #la derivacion se hara respecto a x 

    try:
        # Convierte el texto del usuario en una expresión mataematica de SymPy
        funcion_original = sp.sympify(expresion_str)
        
        print(f"\nFunción Original: f(x) = {funcion_original}")
    
        # Expande la expresión algebraica
        funcion_expandida = sp.expand(funcion_original)
        print(f"Función Expandida: f(x) = {funcion_expandida}")
        
        # Calcula la derivada
        derivada = sp.diff(funcion_original, x)
        print(f"Derivada: f'(x) = {derivada}")
        
        return funcion_original, derivada

    except sp.SympifyError:
        print("\n La expresión ingresada no es válida.")
        print("Asegúrate de usar la sintaxis correcta de Python (ej. 'x**2' en lugar de 'x^2').")
        return None, None

def derivada_por_definicion(f_numerica, punto, h=1e-7): #se usa h=1e-7 como aproximacion al 0 
    """
    Calcula la derivada en un punto usando la fórmula de la diferencia central.
    """
    return (f_numerica(punto + h) - f_numerica(punto - h)) / (2 * h)


def evaluacion_en_punto(funcion_simbolica, derivada_simbolica):
    """
    Pide al usuario un punto y calcula la derivada en ese punto
    usando el método numérico para compararlo con el resultado exacto.
    """
    print("\n--- 2. Evaluación de la Derivada en un Punto ---")
    
    try:
        punto_eval = float(input("Introduce el valor de x donde quieres evaluar la derivada: "))
        
        x = sp.symbols('x')
        f_numerica = sp.lambdify(x, funcion_simbolica, 'numpy') #combierte funcion simbolica a numerica 
        
        valor_derivada_numerica = derivada_por_definicion(f_numerica, punto_eval)
        print(f"Resultado numérico (por definición) en x={punto_eval}: {valor_derivada_numerica:.6f}")

        valor_real = derivada_simbolica.subs(x, punto_eval).evalf()
        print(f"Resultado exacto (usando SymPy) en x={punto_eval}: {valor_real}")

    except (ValueError, TypeError):
        print("Error: Por favor, introduce un número válido.")


# --- Ejecución del Programa ---
if __name__ == "__main__":
    # Llama a la primera parte para obtener las funciones simbólicas
    f_original, f_derivada = operaciones_simbolicas()
    
    # Si la función se creó correctamente, procede a la segunda parte
    if f_original is not None:
        evaluacion_en_punto(f_original, f_derivada)
