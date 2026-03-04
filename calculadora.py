# Librerias


# Funciones
def validar_tipo(valor_primero, valor_segundo):
    if not isinstance(valor_primero, (float, int)):
        raise TypeError("Error de Tipo: El valor ingresado no es un número")
    if not isinstance(valor_segundo, (float, int)):
        raise TypeError("Error de Tipo: El valor ingresado no es un número")


# Clases
class Calculadora:
    """
    Este es el objeto calculadora, que tiene de unico atributo el historial
    iniciara con 4 metodos fundamentales, sumar, restar, multiplicar y dividir.
    Además, tenemos un metodo para mostrar todo el historial guardado.
    De esta forma se cumple la logica interna de una calculadora.
    """

    def __init__(self):
        self.__historial = []

    # Metodo privado para guardar las operaciones
    def __guardar_operacion(
        self,
        valor_primero: float,
        valor_segundo: float,
        resultado: float,
        operacion: str,
    ):
        self.__historial.append(
            f"{valor_primero} {operacion} {valor_segundo} = {resultado}"
        )

    # Metodo para sumar
    def sumar(self, primer_valor: float, segundo_valor: float):
        """
        Tenemos el metodo de sumar
         1: Recibimos 2 valores
         2: Validamos que sean de tipo entero o flotante
         3: Almacenamos los valores con el metodo correspondiente
         4: Retornamos el resultado de la operación
        """
        validar_tipo(primer_valor, segundo_valor)
        resultado = primer_valor + segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "+")
        return resultado

    # Metodo para restar
    def restar(self, primer_valor: float, segundo_valor: float):
        """
        Tenemos el metodo de restar
         1: Recibimos 2 valores
         2: Validamos que sean de tipo entero o flotante
         3: Almacenamos los valores con el metodo correspondiente
         4: Retornamos el resultado de la operación
        """
        validar_tipo(primer_valor, segundo_valor)
        resultado = primer_valor - segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "-")
        return resultado

    # Metodo para dividir

    def dividir(self, primer_valor: float, segundo_valor: float):
        """
        Tenemos el metodo de dividir
         1: Recibimos 2 valores
         2: Validamos que sean de tipo entero o flotante
         3: Validamos que el segundo valor no sea 0
         4: Almacenamos los valores con el metodo correspondiente
         5: Retornamos el resultado de la operación
        """
        validar_tipo(primer_valor, segundo_valor)
        if not segundo_valor:
            raise ValueError("Error de valor: No se puede dividir entre cero")
        resultado = primer_valor / segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "/")
        return resultado

    # Metodo para multiplicar
    def multiplicar(self, primer_valor: float, segundo_valor: float):
        """
        Tenemos el metodo de multiplicar
         1: Recibimos 2 valores
         2: Validamos que sean de tipo entero o flotante
         3: Almacenamos los valores con el metodo correspondiente
         4: Retornamos el resultado de la operación
        """
        validar_tipo(primer_valor, segundo_valor)
        resultado = primer_valor * segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "x")
        return resultado

    # Metodo para mostrar todo el historial
    def mostrar_historial(self):
        """
        Tenemos el metodo mostrar historial para el atributo privado de
        historial.
        """
        print("Historial de la calculadora")
        for operacion in self.__historial:
            print(operacion)
