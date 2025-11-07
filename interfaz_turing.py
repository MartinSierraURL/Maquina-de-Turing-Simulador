import tkinter as tk
import time
from expresiones import EXPRESIONES, evaluar_regex
from maquinas import MT_1, MT_2, MT_3, MT_4, MT_5

class InterfazTuring:
    def __init__(self, ventana, maquina=None):
        self.ventana = ventana
        self.maquina = maquina

        # Sección superior
        frame_superior = tk.Frame(ventana)
        frame_superior.pack(pady=10)

        tk.Label(frame_superior, text="Selecciona una expresión:").grid(row=0, column=0)

        opciones = [f"{i+1}) {desc}" for i, (desc, _) in enumerate(EXPRESIONES)]
        self.var_expr = tk.StringVar(value=opciones[0])
        tk.OptionMenu(frame_superior, self.var_expr, *opciones).grid(row=0, column=1)

        tk.Label(frame_superior, text="Cadena:").grid(row=1, column=0)
        self.entrada = tk.Entry(frame_superior, width=25)
        self.entrada.grid(row=1, column=1)

        tk.Button(frame_superior, text="Probar expresión", command=self.probar).grid(row=1, column=2, padx=10)

        self.label_resultado = tk.Label(frame_superior, text="", font=("Arial", 12))
        self.label_resultado.grid(row=2, column=0, columnspan=3, pady=5)

        tk.Frame(ventana, height=2, bd=1, relief="sunken").pack(fill="x", pady=10)

        # Cinta
        self.label_cinta = tk.Label(ventana, font=("Consolas", 18))
        self.label_cinta.pack(pady=10)

        # Estado
        self.label_estado = tk.Label(ventana, font=("Arial", 14))
        self.label_estado.pack()

        # Botones
        botones = tk.Frame(ventana)
        botones.pack(pady=10)
        tk.Button(botones, text="Paso", command=self.paso).pack(side="left", padx=10)
        tk.Button(botones, text="Automático", command=self.automatico).pack(side="right", padx=10)

        self.actualizar()

    def probar(self):
        texto = self.entrada.get().strip()
        indice = int(self.var_expr.get().split(")")[0]) - 1

        if evaluar_regex(texto, indice):
            self.label_resultado.config(text="✅ La cadena cumple la expresión.", fg="green")

            maquinas = [MT_1, MT_2, MT_3, MT_4, MT_5]
            self.maquina = maquinas[indice](texto)
            self.actualizar()

        else:
            self.label_resultado.config(text="❌ La cadena NO cumple la expresión.", fg="red")

    def actualizar(self):
        if not self.maquina:
            self.label_cinta.config(text="(Cinta no cargada aún)")
            self.label_estado.config(text="Estado actual: -")
            return

        cinta = ""
        for i, simbolo in enumerate(self.maquina.cinta):
            cinta += f"[{simbolo}]" if i == self.maquina.cabezal else f" {simbolo} "
        self.label_cinta.config(text=cinta)
        self.label_estado.config(text=f"Estado actual: {self.maquina.estado}")

    def paso(self):
        if self.maquina and not (self.maquina.es_aceptada() or self.maquina.es_rechazada()):
            self.maquina.paso()
            self.actualizar()

    def automatico(self):
        if self.maquina:
            while not (self.maquina.es_aceptada() or self.maquina.es_rechazada()):
                self.maquina.paso()
                self.actualizar()
                self.ventana.update()
                time.sleep(0.5)
