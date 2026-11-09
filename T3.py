import math
import random


def punto_aleatorio(a, b):
    # Punto decimal aleatorio dentro del rectángulo
    x = a * (2 * random.random() - 1)
    y = b * (2 * random.random() - 1)
    return x, y


def en_elipse(x, y, a, b):
    return x * x / (a * a) + y * y / (b * b) <= 1


def en_hiperbola(x, y, c, d):
    return x * x / (c * c) - y * y / (d * d) >= 1


def leer_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser un numero positivo.")
        except ValueError:
            print("  Entrada invalida, escriba un numero.")


def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser un entero positivo.")
        except ValueError:
            print("  Entrada invalida, escriba un numero entero.")


def main():
    print("=== Area de la elipse que se interseca con la hiperbola (Monte Carlo) ===")
    a = leer_positivo("a (semieje de la elipse en x): ")
    b = leer_positivo("b (semieje de la elipse en y): ")
    c = leer_positivo("c (constante de la hiperbola en x): ")
    d = leer_positivo("d (constante de la hiperbola en y): ")
    cantidad = leer_entero_positivo("Cantidad de numeros aleatorios: ")

    puntos_elipse = 0
    puntos_interseccion = 0

    # Generación de puntos aleatorios dentro del rectángulo que contiene la elipse
    for _ in range(cantidad):
        x, y = punto_aleatorio(a, b)

        # Verificar si pertenece a la elipse
        if en_elipse(x, y, a, b):
            puntos_elipse += 1

            # Verificar si pertenece a la hipérbola (intersección)
            if en_hiperbola(x, y, c, d):
                puntos_interseccion += 1

    # Área de la elipse por fórmula
    area_elipse = math.pi * a * b

    print("\n--- Resultados ---")
    print(f"Puntos generados (rectangulo)      : {cantidad}")
    print(f"Puntos dentro de la elipse         : {puntos_elipse}")
    print(f"Puntos en la interseccion          : {puntos_interseccion}")
    print(f"Area de la elipse (pi*a*b)         : {area_elipse:.4f}")

    if puntos_elipse == 0:
        print("Ningun punto cayo en la elipse; use mas puntos.")
        return

    # Regla de 3
    proporcion = puntos_interseccion / puntos_elipse
    area_interseccion = area_elipse * proporcion

    print(f"Proporcion interseccion / elipse   : {proporcion:.4f}")
    print(f"Area aproximada de la interseccion : {area_interseccion:.4f}")


if __name__ == "__main__":
    main()