import tkinter
from tkinter import ttk, font


class Aplicacion:
    def __init__(self):
        self.raiz = tkinter.Tk()
        self.raiz.title("Sumar")

        fuente = font.Font(weight='bold')

        self.etiq1 = ttk.Label(self.raiz, text="FALTA DISEÑO ", font=fuente)
        self.etiq2 = ttk.Label(self.raiz, text="FALTA DISEÑO ", font=fuente)
        self.etiq3 = ttk.Label(self.raiz, text="FALTA DISEÑO ", font=fuente)
        self.etiq4 = ttk.Label(self.raiz, text="FALTA DISEÑO ", font=fuente)
        self.etiq5 = ttk.Label(self.raiz, text="FALTA DISEÑO", font=fuente)

        self.ctext1 = ttk.Entry(self.raiz, width=30)
        self.ctext2 = ttk.Entry(self.raiz, width=30)
        self.ctext3 = ttk.Entry(self.raiz, width=30)
        self.ctext4 = ttk.Entry(self.raiz, width=30)
        self.ctext5 = ttk.Entry(self.raiz, width=30)

        self.separador = ttk.Separator(self.raiz, orient=tkinter.HORIZONTAL)

        self.boton1 = ttk.Button(self.raiz, text="Calcular",
                command=self.calcular)
        self.boton2 = ttk.Button(self.raiz, text="Salir", command=quit)

        self.texto_resultado = tkinter.StringVar()
        self.texto_resultado.set('... ...')
        self.resultado = ttk.Label(self.raiz, textvariable=self.texto_resultado,
                font=fuente)

        self.etiq1.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)
        self.ctext1.pack(side=tkinter.TOP, fill=tkinter.X, expand=True,
                padx=5, pady=5)
        self.etiq2.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)
        self.ctext2.pack(side=tkinter.TOP, fill=tkinter.X, expand=True,
                padx=5, pady=5)
        self.etiq3.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)
        self.ctext3.pack(side=tkinter.TOP, fill=tkinter.X, expand=True,
                padx=5, pady=5)
        self.etiq4.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)
        self.ctext4.pack(side=tkinter.TOP, fill=tkinter.X, expand=True,
                padx=5, pady=5)
        self.etiq5.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)
        self.ctext5.pack(side=tkinter.TOP, fill=tkinter.X, expand=True,
                padx=5, pady=5)

        self.separador.pack(side=tkinter.TOP, fill=tkinter.X, expand=True,
                padx=5, pady=5)

        self.resultado.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)

        self.boton1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)
        self.boton2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True,
                padx=5, pady=5)

        self.ctext1.focus_set()

        self.raiz.bind('<Return>', self.calcular)

        self.raiz.mainloop()




def main():
    mi_programa = Aplicacion()
    return 0

if __name__ == "__main__":
     main()
