"""Módulo de la calculadora.

Este módulo define la función de validación de tipos y la clase Calculadora,
que permite realizar operaciones aritméticas básicas con historial.
"""


def validar_tipo(valor_primero: float, valor_segundo: float) -> None:
    """Valida que ambos valores sean de tipo int o float.

    Args:
        valor_primero: Primer valor a validar.
        valor_segundo: Segundo valor a validar.

    Raises:
        TypeError: Si alguno de los valores no es numérico.
    """
    if not isinstance(valor_primero, (float, int)):
        raise TypeError("Error de Tipo: El valor ingresado no es un número")
    if not isinstance(valor_segundo, (float, int)):
        raise TypeError("Error de Tipo: El valor ingresado no es un número")


class Calculadora:
    """Objeto calculadora con historial de operaciones.

    Provee cuatro operaciones aritméticas básicas: sumar, restar,
    multiplicar y dividir. Cada operación queda registrada en un
    historial interno accesible mediante `mostrar_historial`.
    """

    def __init__(self) -> None:
        """Inicializa la calculadora con un historial vacío."""
        self.__historial = []

    def __guardar_operacion(
        self,
        valor_primero: float,
        valor_segundo: float,
        resultado: float,
        operacion: str,
    ) -> None:
        """Guarda una operación realizada en el historial interno.

        Args:
            valor_primero: Primer operando de la operación.
            valor_segundo: Segundo operando de la operación.
            resultado: Resultado obtenido.
            operacion: Símbolo que representa la operación realizada.
        """
        self.__historial.append(
            f"{valor_primero} {operacion} {valor_segundo} = {resultado}"
        )

    def sumar(self, primer_valor: float, segundo_valor: float) -> float:
        """Suma dos valores numéricos.

        Args:
            primer_valor: Primer operando.
            segundo_valor: Segundo operando.

        Returns:
            El resultado de la suma.

        Raises:
            TypeError: Si alguno de los valores no es numérico.
        """
        validar_tipo(primer_valor, segundo_valor)
        resultado = primer_valor + segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "+")
        return resultado

    def restar(self, primer_valor: float, segundo_valor: float) -> float:
        """Resta dos valores numéricos.

        Args:
            primer_valor: Primer operando.
            segundo_valor: Segundo operando.

        Returns:
            El resultado de la resta.

        Raises:
            TypeError: Si alguno de los valores no es numérico.
        """
        validar_tipo(primer_valor, segundo_valor)
        resultado = primer_valor - segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "-")
        return resultado

    def dividir(self, primer_valor: float, segundo_valor: float) -> float:
        """Divide dos valores numéricos.

        Args:
            primer_valor: Dividendo.
            segundo_valor: Divisor.

        Returns:
            El resultado de la división.

        Raises:
            TypeError: Si alguno de los valores no es numérico.
            ValueError: Si el divisor es cero.
        """
        validar_tipo(primer_valor, segundo_valor)
        if segundo_valor == 0:
            raise ValueError("Error de valor: No se puede dividir entre cero")
        resultado = primer_valor / segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "/")
        return resultado

    def multiplicar(self, primer_valor: float, segundo_valor: float) -> float:
        """Multiplica dos valores numéricos.

        Args:
            primer_valor: Primer operando.
            segundo_valor: Segundo operando.

        Returns:
            El resultado de la multiplicación.

        Raises:
            TypeError: Si alguno de los valores no es numérico.
        """
        validar_tipo(primer_valor, segundo_valor)
        resultado = primer_valor * segundo_valor
        self.__guardar_operacion(primer_valor, segundo_valor, resultado, "x")
        return resultado

    def mostrar_historial(self) -> list:
        """Retorna una copia del historial de operaciones realizadas.

        Returns:
            Lista de strings con cada operación registrada.
        """
        return self.__historial.copy()
