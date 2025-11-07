from tkinter import Tk
from maquina_turing import MaquinaTuring
from interfaz_turing import InterfazTuring

if __name__ == "__main__":

    # Transiciones para aceptar "abb"
    transiciones = {
        ('q0', 'a'): ('a', 'R', 'q0'),
        ('q0', 'b'): ('b', 'R', 'q1'),
        ('q1', 'b'): ('b', 'R', 'qA')
    }

    maquina = MaquinaTuring("abb", transiciones, "q0", "qA", "qR")

    ventana = Tk()
    ventana.title("Simulador de Máquina de Turing")

    interfaz = InterfazTuring(ventana, maquina)

    ventana.mainloop()
