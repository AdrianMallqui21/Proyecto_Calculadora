# Librerias
import calculadora as c


# Funciones
def validar_numero(texto):
    while 1:
        try:
            numero = float(input(texto))
            return numero
        except ValueError:
            print("Error: El valor ingresado debe ser un número entero")


def validar_opcion(texto, valor_inf, valor_sup):
    while 1:
        try:
            numero = int(input(texto))
            if valor_inf <= numero <= valor_sup:
                return numero
            else:
                print(f"La opción debe estar entre {valor_inf} y {valor_sup}")
        except ValueError:
            print("Error: El valor ingresado debe ser un número entero")


def imprimir_opciones():
    print(f"{"#"*20}")
    print("Calculadora de Adrian")
    print(f"{"#"*20}")
    print("1: Sumar")
    print("2: Restar")
    print("3: Multiplicar")
    print("4: Dividir")
    print("5: Historial")
    print("6: Fin")


def main():
    calcular = c.Calculadora()
    while 1:
        imprimir_opciones()
        opcion = validar_opcion("Elige una opción: ", 1, 6)
        match opcion:
            case 1:  # Sumar
                try:
                    print(f"\n{"#"*20}")
                    print("Suma")
                    print(f"{"#"*20}")
                    numero_1 = validar_numero("Ingresa el primer número: ")
                    numero_2 = validar_numero("Ingresa el segundo número: ")
                    resultado = calcular.sumar(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} + {numero_2} = {resultado}")
                except TypeError as e:
                    print(e)
            case 2:  # Restar
                try:
                    print(f"\n{"#"*20}")
                    print("Resta")
                    print(f"{"#"*20}")
                    numero_1 = validar_numero("Ingresa el primer número: ")
                    numero_2 = validar_numero("Ingresa el segundo número: ")
                    resultado = calcular.restar(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} - {numero_2} = {resultado}")
                except TypeError as e:
                    print(e)
            case 3:  # Multiplicar
                try:
                    print(f"\n{"#"*20}")
                    print("Multiplicación")
                    print(f"{"#"*20}")
                    numero_1 = validar_numero("Ingresa el primer número: ")
                    numero_2 = validar_numero("Ingresa el segundo número: ")
                    resultado = calcular.multiplicar(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} X {numero_2} = {resultado}")
                except TypeError as e:
                    print(e)
            case 4:  # Dividir
                try:
                    print(f"\n{"#"*20}")
                    print("Division")
                    print(f"{"#"*20}")
                    numero_1 = validar_numero("Ingresa el primer número: ")
                    numero_2 = validar_numero("Ingresa el segundo número: ")
                    resultado = calcular.dividir(
                        primer_valor=numero_1, segundo_valor=numero_2
                    )
                    print(f"{numero_1} / {numero_2} = {resultado}")
                except ValueError as e:
                    print(e)
            case 5:  # Historial
                calcular.mostrar_historial()
        if opcion == 6:
            break


# Clases

# Principal
if __name__ == "__main__":
    main()
