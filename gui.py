from alumnado import Alumnado
from repositorio_alumnado import RepositorioAlumnado
from alumno import Alumno
import tkinter
from tkinter import ttk
from tkinter import messagebox

class Gui():
    
    def __init__(self):
        self.iniciar_alumnado()
        self.iniciar_gui()

    def iniciar_alumnado(self):
        self.repositorio_alumnado = RepositorioAlumnado()
        alumnado = self.repositorio_alumnado.obtener_todo()
        self.alumnado = Alumnado(alumnado)

    def iniciar_gui(self):
        '''Crear la pantalla inicial, mostrando todos los alumnos y botones'''
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("Clases de Música")
        botonAgregar=tkinter.Button(self.ventana_principal,text="Agregar alumno", 
                           command = self.agregar_alumno).grid(row=2, column=1)
        botonModificar=tkinter.Button(self.ventana_principal,text="Modificar",
                           command = self.modificar_alumno).grid(row=2, column=2)
        botonEliminar=tkinter.Button(self.ventana_principal, text = "Eliminar",
                           command = self.eliminar_alumno).grid(row=2, column=0)
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1, sticky="ew")
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar alumno",
                           command = self.buscar_alumnos).grid(row=1, column=2, sticky="w")

        instrumentos = ['Guitarra', 'Bajo', 'Flauta']
        filtro_elegido = tkinter.StringVar(self.ventana_principal)
        filtro_elegido.set(instrumentos[0]) # default value
        self.buscar_filtro = ttk.OptionMenu(self.ventana_principal, filtro_elegido, '', *instrumentos, command=self.buscar_instrumento)
        self.buscar_filtro.grid(row=2, column=3)

        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal,
        columns=("nombre", "dia_dictado", "horario_dictado", "instrumento"))
        self.treeview.heading("#0", text="Dni")
        self.treeview.column("#0", minwidth=0)

        self.treeview.heading("nombre", text="Nombre")

        self.treeview.heading("dia_dictado", text="Dia de dictado")

        self.treeview.heading("horario_dictado", text="Horario")

        self.treeview.heading("instrumento", text="Instrumento")
        self.treeview.grid(row=10, columnspan=4)
        self.poblar_tabla()
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)
        self.cajaBuscar.focus()

    def poblar_tabla(self, alumnos = None):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        '''Si no recibimos la lista del alumnado, le asignamos todos las alumnos:'''
        if not alumnos:
            alumnos = self.alumnado.alumnos
        '''Poblamos la lista alumnos:'''
        for alumno in alumnos:
            item = self.treeview.insert("", tkinter.END, text=alumno.dni,
                              values=(alumno.nombre, alumno.dia_dictado, alumno.horario_dictado, alumno.instrumento), iid=alumno.dni)
        
    def agregar_alumno(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Dni: ").grid(row=0)
        self.dni = tkinter.Entry(self.modalAgregar)
        self.dni.grid(row=0, column=1, columnspan=2)
        self.dni.focus()
        tkinter.Label(self.modalAgregar, text = "Alumno: ").grid(row=1)
        self.nombre = tkinter.Entry(self.modalAgregar)
        self.nombre.grid(row=1,column=1,columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Dia de dictado (XXXX/MM/DD): ").grid(row=2)
        self.dia_dictado = tkinter.Entry(self.modalAgregar)
        self.dia_dictado.grid(row=2, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Horario dictado (HH:MM): ").grid(row=3)
        self.horario_dictado = tkinter.Entry(self.modalAgregar)
        self.horario_dictado.grid(row=3, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Instrumento: ").grid(row=4)
        self.instrumento = tkinter.Entry(self.modalAgregar)
        self.instrumento.grid(row=4, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalAgregar, text="Guardar alumno",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=5)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=5, column=2)

    def agregar_ok(self, event=None):
        '''Validamos el ingreso el alumno'''
        alumno = self.alumnado.nuevo_alumno(self.dni.get(), self.nombre.get(), self.dia_dictado.get(), self.horario_dictado.get(), self.instrumento.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=alumno.dni,
        values=(alumno.nombre, alumno.dia_dictado, alumno.horario_dictado, alumno.instrumento))

    def modificar_alumno(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el alumno a modificar")
            return False
        #id = int(self.treeview.selection()[0][1:])
        item = self.treeview.selection()
        dni = self.treeview.item(item)['text']
        alumno = self.alumnado._buscar_por_dni(dni)
        dni = self.treeview.item(item, option="text")

        self.modalModificar = tkinter.Toplevel(self.ventana_principal)
        self.modalModificar.grab_set()

        tkinter.Label(self.modalModificar, text = "Alumno: ").grid(row=1)
        self.nombre = tkinter.Entry(self.modalModificar)
        self.nombre.insert(0,alumno.nombre)
        self.nombre.grid(row=1, column=1, columnspan=2)

        tkinter.Label(self.modalModificar, text = "Dia de dictado: ").grid(row=2)
        self.dia_dictado = tkinter.Entry(self.modalModificar)
        self.dia_dictado.insert(0,alumno.dia_dictado)
        self.dia_dictado.grid(row=2, column=1, columnspan=2)

        tkinter.Label(self.modalModificar, text = "Horario: ").grid(row=3)
        self.horario_dictado = tkinter.Entry(self.modalModificar)
        self.horario_dictado.insert(0,alumno.horario_dictado)
        self.horario_dictado.grid(row=3, column=1, columnspan=2)

        tkinter.Label(self.modalModificar, text = "Instrumento: ").grid(row=4)
        self.instrumento = tkinter.Entry(self.modalModificar)
        self.instrumento.insert(0,alumno.instrumento)
        self.instrumento.grid(row=4, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalModificar, text="Guardar",
                command=self.modificar_ok)
        self.modalModificar.bind("<Return>", self.modificar_ok)
        botonOK.grid(row=5)
        botonCancelar = tkinter.Button(self.modalModificar, text = "Cancelar",
                                       command = self.modalModificar.destroy)
        botonCancelar.grid(row=5, column=2)

    def modificar_ok(self, event=None):
        '''Valida la modificacion de los datos'''
        item = self.treeview.selection()        
        dni = self.treeview.item(item)['text']
        nombre_temp = self.nombre.get()
        dia_temp = self.dia_dictado.get()
        horario_temp = self.horario_dictado.get()
        instrumento_temp = self.instrumento.get()
        
        self.alumnado.modificar_alumno(dni, nombre_temp, dia_temp, horario_temp, instrumento_temp)
        self.treeview.set(self.treeview.selection()[0], column="nombre",
                          value = nombre_temp)
        self.treeview.set(self.treeview.selection()[0], column="dia_dictado",
                          value = dia_temp)
        self.treeview.set(self.treeview.selection()[0], column="horario_dictado",
                          value = horario_temp)
        self.treeview.set(self.treeview.selection()[0], column="instrumento",
                          value = instrumento_temp)
        self.modalModificar.destroy()

    def eliminar_alumno(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el alumno a eliminar de la lista")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                    "¿Está seguro de eliminar el alumno de la lista?")
            if resp:
                item = self.treeview.selection()
                dni = self.treeview.item(item)['text']
                alumno = self.alumnado._buscar_por_dni(dni)
                if alumno:
                    if self.alumnado.eliminar_alumno(dni):
                        self.treeview.delete(dni)
                    else:
                        messagebox.showwarning(
                            "Error al eliminar")
                print(alumno.nombre + 'alumno eliminado')#probar
            else:
                return False

    def buscar_alumnos(self):
        filtro = self.cajaBuscar.get()
        alumnado = self.alumnado.buscar(filtro)
        if alumnado:
            self.poblar_tabla(alumnado)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ningun alumno coincide con la búsqueda")

    def buscar_instrumento(self, filtro):
        '''Aqui se filtraran los alumnos por instrumento a travez de un desplegable'''
        alumnado = self.alumnado.filtrar(filtro)
        if alumnado:
            self.poblar_tabla(alumnado)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ningun instrumento coincide con la búsqueda")
    
    def salir(self):
        self.repositorio_alumnado.guardar_todo(self.alumnado.alumnos)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()
