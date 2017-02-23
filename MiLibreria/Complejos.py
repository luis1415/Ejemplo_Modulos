# -*- coding: utf-8 -*-
class NumeroComplejo(object):
    """
    Clase para Trabajar con numeros complejos
    """

    # Constructor
    def __init__(self, x1, y1):
        """
        Constructor de numeros complejos
        """
        self.x = x1
        self.y = y1

    # Metodos
    def __le__(self, otrocomplejo):
        """
        Esta función sobrescribe el menor o igual.
        :param otrocomplejo: es otro objeto de la clase numero complejo
        :return: verdadero o falso
        """
        return self.x <= otrocomplejo.x and self.y <= otrocomplejo.y

    def __add__(self, otrocomplejo):
        return NumeroComplejo(self.x + otrocomplejo.x, self.y + otrocomplejo.y)

    def __sub__(self, otrocomplejo):
        return NumeroComplejo(self.x - otrocomplejo.x, self.y - otrocomplejo.y)

    def __str__(self):
        return '({} , {}i)'.format(self.x, self.y)

    def __eq__(self, otrocomplejo):
        return self.x == otrocomplejo.x and self.y == otrocomplejo.y

    def __gt__(self, otrocomplejo):
        """
        esta función es para comparar dos numeros complejos con >
        :param otrocomplejo: es otro número complejo
        :return: Falso o Verdadero
        """
        return self.x > otrocomplejo.x and self.y > otrocomplejo.y
