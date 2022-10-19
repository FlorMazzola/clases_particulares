from alumnado import Alumnado
from repositorio_alumnado import RepositorioAlumnado
from alumno import Alumno
import tkinter
from tkinter import ttk
from tkinter import messagebox

class Gui():
    '''Crear la pantalla inicial, mostrando todas las notas y botones'''
    def __init__(self):
        self.iniciar_alumnado()
        self.iniciar_gui()

    def iniciar_alumnado(self):
        self.repositorio_alumnado = RepositorioAlumnado()
        alumnado = self.repositorio_alumnado.obtener_todo()
        self.alumnado = Alumnado(alumnado)

    def iniciar_gui(self):
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("Clases de Guitarra")
        botonAgregar=tkinter.Button(self.ventana_principal,text="Agregar alumno", 
                           command = self.agregar_alumno).grid(row=2, column=1)
        botonModificar=tkinter.Button(self.ventana_principal,text="Modificar",
                           command = self.modificar_alumno).grid(row=2, column=2)
        botonEliminar=tkinter.Button(self.ventana_principal, text = "Eliminar",
                           command = self.eliminar_alumno).grid(row=2, column=0)
#        tkinter.Label(self.ventana_principal,text="Escuela de Musica").grid(row=0, column=2)
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1, sticky="ew")
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar alumno",
                           command = self.buscar_alumnos).grid(row=1, column=2, sticky="w")
        #self.tabla = ttk.Treeview(self,
        #column = ('Nombre', 'Instrumento', 'Día de dictado'))
        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal,
        columns=("texto", "dia_dictado"))
        self.treeview.heading("#0", text="Dni")
        #self.treeview.column("#0", minwidth=0, width="40")
        self.treeview.heading("texto", text="Nombre")
        #self.treeview.config(font=('Arial', 23 , 'Bold'))
        self.treeview.heading("dia_dictado", text="Dia de dictado")
        self.treeview.grid(row=10, columnspan=3)
        self.poblar_tabla()
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)
        self.cajaBuscar.focus()

    def poblar_tabla(self, alumnos = None):
        #Vaciamos el Treeview, si tuviera algún item:
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        #Si no recibimos la lista de alumnado, le asignamos todas las alumnado:
        if not alumnos:
            alumnos = self.alumnado.alumnos
        #Poblamos el treeview:
        for alumno in alumnos:
            item = self.treeview.insert("", tkinter.END, text=alumno.dni,
                              values=(alumno.nombre, alumno.dia_dictado), iid=alumno.dni)
        
    def agregar_alumno(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        #top.transient(parent)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Alumno: ").grid()
        self.nombre = tkinter.Entry(self.modalAgregar)
        self.nombre.grid(row=0,column=1,columnspan=2)
        self.nombre.focus()
        tkinter.Label(self.modalAgregar, text = "Dia de dictado: ").grid(row=1)
        self.dia_dictado = tkinter.Entry(self.modalAgregar)
        self.dia_dictado.grid(row=1, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalAgregar, text="Guardar alumno",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=2)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=2,column=2)

    def agregar_ok(self, event=None):
        alumno = self.alumnado.nuevo_alumno(self.alumno.get(), self.dia_dictado.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=alumno.dni,
        values=(alumno.nombre, alumno.dia_dictado))
        #print(self.treeview.set(item))

    def modificar_alumno(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el alumno a modificar")
            return False
        #id = int(self.treeview.selection()[0][1:])
        item = self.treeview.selection()        
        dni = self.treeview.item(item)['text']
        #id = self.treeview.item(item, option="text")

        #Para probar:
        #print(alumno.dni)

        alumno = self.Alumnado._buscar_por_dni(alumno.dni)
        self.modalModificar = tkinter.Toplevel(self.ventana_principal)
        self.modalModificar.grab_set()
        tkinter.Label(self.modalModificar, text = "Alumno: ").pack()
        self.nombre = tkinter.Entry(self.modalModificar)
        self.nombre.insert(0,alumno.nombre)
        self.nombre.pack()
        self.nombre.focus()
        tkinter.Label(self.modalModificar, text = "Dia de dictado: ").pack()
        self.etiquetas = tkinter.Entry(self.modalModificar)
        self.etiquetas.insert(0,alumno.nombre)
        self.etiquetas.pack()
        botonOK = tkinter.Button(self.modalModificar, text="Guardar",
                command=self.modificar_ok)
        self.modalModificar.bind("<Return>", self.modificar_ok)
        botonOK.pack()
        botonCancelar = tkinter.Button(self.modalModificar, text = "Cancelar",
                                       command = self.modalModificar.destroy)
        botonCancelar.pack()

    def modificar_ok(self, event=None):
        item = self.treeview.selection()        
        id = self.treeview.item(item)['text']
        print("Modificado el horario de cursado",)#dni_alumno)
        #id = int(self.treeview.selection()[0][1:])
        #idtree = self.treeview.selection()[0]
        self.alumnado.modificar_alumno(id, self.nombre.get())
        self.alumnado.modificar_dia_cursado(id, self.etiquetas.get())
        self.treeview.set(self.treeview.selection()[0], column="Nombre",
                          value = self.texto.get())
        self.treeview.set(self.treeview.selection()[0], column="Dia de cursado",
                          value = self.dia_cursado.get())
        self.modalModificar.destroy()
   
    def eliminar_alumno(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el alumno a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                    "¿Está seguro de eliminar el alumno?")
            if resp:
                id = int(self.treeview.selection()[0][1:])
                self.treeview.delete(self.treeview.selection()[0])
                self.alumnado.eliminar_alumno()
            else:
                return False

    def buscar_alumnos(self):
        filtro = self.cajaBuscar.get()
        alumnado = self.alumnado.buscar(filtro)
        if alumnado:
            self.poblar_tabla(alumnado)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ninguna alumno coincide con la búsqueda")
    
    def salir(self):
        self.repositorio_alumnado.guardar_todo(self.alumnado.alumnos)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()
