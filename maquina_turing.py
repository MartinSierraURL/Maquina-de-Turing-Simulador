# Clase que representa la lógica de una Máquina de Turing

class MaquinaTuring:
    def __init__(self, cinta, transiciones, estado_inicial, estado_aceptacion, estado_rechazo):
        # Convertimos la cadena inicial en lista para poder modificarla
        self.cinta = list(cinta) + ['_']   # '_' representa un espacio en blanco
        self.cabezal = 0                   # posición inicial del cabezal
        self.estado = estado_inicial       # estado donde empieza la máquina
        self.estado_aceptacion = estado_aceptacion
        self.estado_rechazo = estado_rechazo
        self.transiciones = transiciones   # diccionario con reglas

    def paso(self):
        """
        Realiza un solo paso de ejecución:
        Lee el símbolo, aplica la transición, escribe y mueve el cabezal.
        """
        simbolo_actual = self.cinta[self.cabezal]

        # Si no existe una regla para (estado, símbolo), la máquina rechaza
        if (self.estado, simbolo_actual) not in self.transiciones:
            self.estado = self.estado_rechazo
            return

        nuevo_simbolo, direccion, nuevo_estado = self.transiciones[(self.estado, simbolo_actual)]

        # Escribir el nuevo símbolo en la cinta
        self.cinta[self.cabezal] = nuevo_simbolo

        # Cambiar al nuevo estado
        self.estado = nuevo_estado

        # Mover el cabezal
        if direccion == 'R':   # Derecha
            self.cabezal += 1
        elif direccion == 'L': # Izquierda
            self.cabezal -= 1
            if self.cabezal < 0:
                self.cabezal = 0  # evita salirnos de la cinta

    def es_aceptada(self):
        """Retorna True si la cadena ha sido aceptada."""
        return self.estado == self.estado_aceptacion

    def es_rechazada(self):
        """Retorna True si la cadena ha sido rechazada."""
        return self.estado == self.estado_rechazo
