"""Lógica de consola para la calculadora.

Este módulo define funciones de validación de entrada y el flujo principal
del programa, gestionando la interacción del usuario con la calculadora.
"""

import calculadora as c


def validar_numero(texto: str) -> float:
    """Solicita al usuario un número flotante y lo valida.

    Args:
        texto: Mensaje a mostrar en la petición de entrada.

    Returns:
        El número ingresado por el usuario.
    """
    while True:
        try:
            numero = float(input(texto))
            return numero
        except ValueError:
            print("Error: El valor ingresado debe ser un número entero")


def validar_opcion(texto: str, valor_inf: int, valor_sup: int) -> int:
    """Valida que una opción numérica ingresada esté dentro de un rango.

    Args:
        texto: Mensaje a mostrar en la petición de entrada.
        valor_inf: Valor mínimo aceptado.
        valor_sup: Valor máximo aceptado.

    Returns:
        La opción seleccionada por el usuario.
    """
    while True:
        try:
            numero = int(input(texto))
            if valor_inf <= numero <= valor_sup:
                return numero
            print(f"La opción debe estar entre {valor_inf} y {valor_sup}")
        except ValueError:
            print("Error: El valor ingresado debe ser un número entero")


def imprimir_opciones() -> None:
    """Imprime el menú de opciones disponible para el usuario."""
    separador = "#" * 20
    print(separador)
    print("Calculadora de Adrian")
    print(separador)
    print("1: Sumar")
    print("2: Restar")
    print("3: Multiplicar")
    print("4: Dividir")
    print("5: Historial")
    print("6: Fin")


def _solicitar_operandos(titulo: str) -> tuple[float, float]:
    """Muestra el encabezado de operación y solicita dos operandos al usuario.

    Args:
        titulo: Nombre de la operación a mostrar como encabezado.

    Returns:
        Tupla con los dos valores ingresados por el usuario.
    """
    separador = "#" * 20
    print(f"\n{separador}")
    print(titulo)
    print(separador)
    numero_1 = validar_numero("Ingresa el primer número: ")
    numero_2 = validar_numero("Ingresa el segundo número: ")
    return numero_1, numero_2


def main() -> None:
    """Ejecuta el flujo principal de la calculadora en consola."""
    calcular = c.Calculadora()
    while True:
        imprimir_opciones()
        opcion = validar_opcion("Elige una opción: ", 1, 6)
        match opcion:
            case 1:
                try:
                    numero_1, numero_2 = _solicitar_operandos("Suma")
                    resultado = calcular.sumar(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} + {numero_2} = {resultado}")
                except (TypeError, ValueError) as e:
                    print(e)
            case 2:
                try:
                    numero_1, numero_2 = _solicitar_operandos("Resta")
                    resultado = calcular.restar(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} - {numero_2} = {resultado}")
                except (TypeError, ValueError) as e:
                    print(e)
            case 3:
                try:
                    numero_1, numero_2 = _solicitar_operandos("Multiplicación")
                    resultado = calcular.multiplicar(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} x {numero_2} = {resultado}")
                except (TypeError, ValueError) as e:
                    print(e)
            case 4:
                try:
                    numero_1, numero_2 = _solicitar_operandos("División")
                    resultado = calcular.dividir(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} / {numero_2} = {resultado}")
                except (TypeError, ValueError) as e:
                    print(e)
            case 5:
                historial = calcular.mostrar_historial()
                print("\nHistorial de la calculadora:")
                for operacion in historial:
                    print(operacion)
            case 6:
                break


if __name__ == "__main__":
    main()
