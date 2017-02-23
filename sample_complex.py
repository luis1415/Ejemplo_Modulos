# -*- coding: utf-8 -*-
import MiLibreria.Complejos as Complejo

if __name__ == '__main__':
    # Instanciando los objetos
    c1 = Complejo.NumeroComplejo(2, 3)
    c2 = Complejo.NumeroComplejo(1, 1)
    print("--------Objetos--------")
    print("Complejo 1:", c1)
    print("Complejo 2:", c2)
    # Acceso a los atributos
    print("--------Atributos--------")
    print("c1 parte real: ", c1.x)
    print("c1 parte imaginaria: ", c1.y)
    print("c2 parte real: ", c2.x)
    print("c2 parte imaginaria: ", c2.y)
    print("--------Métodos--------")
    print(c1 == c2)
    print(c1 + c2)
