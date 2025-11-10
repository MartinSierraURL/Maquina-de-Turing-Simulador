from maquina_turing import MaquinaTuring

# 1) (a|b)*abb
def MT_1(cadena):
    transiciones = {
        # Avanzamos libremente leyendo a o b mientras buscamos el patrón final
        ('q0', 'a'): ('a', 'R', 'q0'),
        ('q0', 'b'): ('b', 'R', 'q0'),

        # Cuando creemos ver un posible inicio del final "a"
        ('q0', 'a'): ('a', 'R', 'q1'),

        # Confirmamos el primer b del final abb
        ('q1', 'b'): ('b', 'R', 'q2'),

        # Confirmamos el segundo b -> si llega aquí, ACEPTA
        ('q2', 'b'): ('b', 'R', 'qA'),

        # Si en q1 o q2 aparece algo inesperado, regresamos a buscar otra coincidencia
        ('q1', 'a'): ('a', 'R', 'q1'),
        ('q2', 'a'): ('a', 'R', 'q1'),
        ('q2', 'a'): ('a', 'R', 'q1'),

        # Final de la cinta:
        ('q0', '_'): ('_', 'R', 'qR'),  # Si nunca encontramos abb → Rechaza
        ('q1', '_'): ('_', 'R', 'qR'),
        ('q2', '_'): ('_', 'R', 'qR'),
        ('qA', '_'): ('_', 'R', 'qA'),  # Se mantiene aceptada
    }

    return MaquinaTuring(cadena, transiciones, "q0", "qA", "qR")


# 2) 0*1*
def MT_2(cadena):
    transiciones = {
        ('q0', '0'): ('0', 'R', 'q0'),
        ('q0', '1'): ('1', 'R', 'q1'),
        ('q1', '1'): ('1', 'R', 'q1'),

        # Final de la cinta → aceptar
        ('q0', '_'): ('_', 'R', 'qA'),
        ('q1', '_'): ('_', 'R', 'qA'),

        # Si aparece un 0 después de un 1 → rechazar
        ('q1', '0'): ('0', 'R', 'qR'),
    }
    return MaquinaTuring(cadena, transiciones, "q0", "qA", "qR")


# 3) (ab)*
def MT_3(cadena):
    transiciones = {
        ('q0', 'a'): ('a', 'R', 'q1'),
        ('q1', 'b'): ('b', 'R', 'q0'),

        # Fin válido si terminamos en q0
        ('q0', '_'): ('_', 'R', 'qA'),

        # Cualquier otro caso → rechazo
        ('q1', 'a'): ('a', 'R', 'qR'),
        ('q0', 'b'): ('b', 'R', 'qR'),
        ('q1', '_'): ('_', 'R', 'qR'),
    }
    return MaquinaTuring(cadena, transiciones, "q0", "qA", "qR")


# 4) 1(01)*0
def MT_4(cadena):
    transiciones = {
        ('q0', '1'): ('1', 'R', 'q1'),
        ('q1', '0'): ('0', 'R', 'q2'),
        ('q2', '1'): ('1', 'R', 'q1'),

        # Si terminamos justo después del último 0 → aceptar
        ('q2', '_'): ('_', 'R', 'qA'),

        # Otros casos → rechazo
        ('q0', '0'): ('0', 'R', 'qR'),
        ('q1', '1'): ('1', 'R', 'qR'),
        ('q0', '_'): ('_', 'R', 'qR'),
        ('q1', '_'): ('_', 'R', 'qR'),
        ('q2', '0'): ('0', 'R', 'qR'),
    }
    return MaquinaTuring(cadena, transiciones, "q0", "qA", "qR")


# 5) (a+b)*a(a+b)*  --> cadenas que tengan al menos una 'a'
def MT_5(cadena):
    transiciones = {
        ('q0', 'a'): ('a', 'R', 'q1'),  # ya vimos una a
        ('q0', 'b'): ('b', 'R', 'q0'),  # seguimos sin ver a

        ('q1', 'a'): ('a', 'R', 'q1'),
        ('q1', 'b'): ('b', 'R', 'q1'),

        # Final
        ('q1', '_'): ('_', 'R', 'qA'),
        ('q0', '_'): ('_', 'R', 'qR'),
    }
    return MaquinaTuring(cadena, transiciones, "q0", "qA", "qR")
