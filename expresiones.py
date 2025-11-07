import re

EXPRESIONES = [
    ("(a|b)*abb", r"^(?:a|b)*abb$"),
    ("0*1*", r"^0*1*$"),
    ("(ab)*", r"^(?:ab)*$"),
    ("1(01)*0", r"^1(?:01)*0$"),
    ("(a+b)*a(a+b)*", r"^(?:a|b)*a(?:a|b)*$"),
]

def evaluar_regex(cadena, indice):
    """
    Retorna True si la cadena cumple la expresión regular seleccionada.
    """
    patron = EXPRESIONES[indice][1]
    return re.fullmatch(patron, cadena) is not None
