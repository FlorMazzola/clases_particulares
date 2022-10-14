from anotador import Anotador
from repositorioAnotador import RepositorioAnotador
import tkinter
from tkinter import ttk
from tkinter import messagebox

class Gui():
    '''Crear la pantalla inicial, mostrando todas las notas y botones'''
    def __init__(self):
        self.iniciar_anotador()
        self.iniciar_gui()

    def iniciar_anotador(self):
        self.repositorio = RepositorioAnotador()
        notas = self.repositorio.obtener_todo()
        self.anotador = Anotador(notas)

    def iniciar_gui(self):
        self.ventana_principal = tkinter.Tk()
        self.ventana_principal.title("Anotador")
        botonAgregar=tkinter.Button(self.ventana_principal,text="Agregar nota", 
                           command = self.agregar_nota).grid(row=0, column=0)
        botonModificar=tkinter.Button(self.ventana_principal,text="Modificar",
                           command = self.modificar_nota).grid(row=0, column=1)
        botonEliminar=tkinter.Button(self.ventana_principal, text = "Eliminar",
                           command = self.eliminar_nota).grid(row=0, column=2)
        tkinter.Label(self.ventana_principal,text="Buscar").grid(row=1,column=0)
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar",
                           command = self.buscar_notas).grid(row=1, column=2)
        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal, 
                                     columns=("texto", "etiquetas"))
        self.treeview.heading("#0", text="id")
        self.treeview.column("#0", minwidth=0, width="40")
        self.treeview.heading("texto", text="Texto")
        self.treeview.heading("etiquetas", text="Etiquetas")
        self.treeview.grid(row=10, columnspan=3)
        self.poblar_tabla()
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)
        self.cajaBuscar.focus()

    def poblar_tabla(self, notas = None):
        #Vaciamos el Treeview, si tuviera algún item:
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        #Si no recibimos la lista de notas, le asignamos todas las notas:
        if not notas:
            notas = self.anotador.notas
        #Poblamos el treeview:
        for nota in notas:
            item = self.treeview.insert("", tkinter.END, text=nota.id,
                              values=(nota.texto, nota.etiquetas), iid=nota.id)
        
    def agregar_nota(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        #top.transient(parent)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Nota: ").grid()
        self.texto = tkinter.Entry(self.modalAgregar)
        self.texto.grid(row=0,column=1,columnspan=2)
        self.texto.focus()
        tkinter.Label(self.modalAgregar, text = "Etiquetas: ").grid(row=1)
        self.etiquetas = tkinter.Entry(self.modalAgregar)
        self.etiquetas.grid(row=1, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=2)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=2,column=2)

    def agregar_ok(self, event=None):
        nota = self.anotador.nueva_nota(self.texto.get(), self.etiquetas.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=nota.id,
                                        values=(nota.texto, nota.etiquetas))
        #print(self.treeview.set(item))

    def modificar_nota(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero la nota a modificar")
            return False
        #id = int(self.treeview.selection()[0][1:])
        item = self.treeview.selection()        
        id = self.treeview.item(item)['text']
        #id = self.treeview.item(item, option="text")

        #Para probar:
        print(id)

        nota = self.anotador._buscar_por_id(id)
        self.modalModificar = tkinter.Toplevel(self.ventana_principal)
        self.modalModificar.grab_set()
        tkinter.Label(self.modalModificar, text = "Nota: ").pack()
        self.texto = tkinter.Entry(self.modalModificar)
        self.texto.insert(0,nota.texto)
        self.texto.pack()
        self.texto.focus()
        tkinter.Label(self.modalModificar, text = "Etiquetas: ").pack()
        self.etiquetas = tkinter.Entry(self.modalModificar)
        self.etiquetas.insert(0,nota.etiquetas)
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
        print("Modificada la nota ",id)
        #id = int(self.treeview.selection()[0][1:])
        #idtree = self.treeview.selection()[0]
        self.anotador.modificar_nota(id, self.texto.get())
        self.anotador.modificar_etiquetas(id, self.etiquetas.get())
        self.treeview.set(self.treeview.selection()[0], column="texto",
                          value = self.texto.get())
        self.treeview.set(self.treeview.selection()[0], column="etiquetas",
                          value = self.etiquetas.get())
        self.modalModificar.destroy()
   
    def eliminar_nota(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero la nota a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                    "¿Está seguro de eliminar la nota?")
            if resp:
                id = int(self.treeview.selection()[0][1:])
                self.treeview.delete(self.treeview.selection()[0])
                self.anotador.eliminar_nota(id)
            else:
                return False

    def buscar_notas(self):
        filtro = self.cajaBuscar.get()
        notas = self.anotador.buscar(filtro)
        if notas:
            self.poblar_tabla(notas)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ninguna nota coincide con la búsqueda")
    
    def salir(self):
        self.repositorio.guardar_todo(self.anotador.notas)
        self.ventana_principal.destroy()

if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()
