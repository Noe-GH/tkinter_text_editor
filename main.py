import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import traceback

# Global variable that stores the name and the absolute path of the file in use.
opened_file = ""

def opened_file_to_value(value):
    """
    Function that assign a value to the global variable opened_file.
    """
    global opened_file
    opened_file = value


def new_file():
    '''
    Function that deletes the content of the Text() widget that represents the text area of the program.
    '''
    text_area.delete(1.0, tk.END)
    opened_file_to_value("")


def open_file():
    """
    Function that opens a filedialog to open a .txt file and the content of the file is inserted in the Text widget that represents the text area.
    """
    try:
        text_area.delete(1.0, tk.END)
        with filedialog.askopenfile(mode='r', title='Select file', filetypes=[('.txt', '*.txt*')]) as f:
            text_area.insert(tk.END, f.read()[:-1])
            opened_file_to_value(f.name)
    except AttributeError:
        '''
        If no file was selected.
        '''
        return


def save_file_as():
    '''
    Function that gets the content from the Text() widget and creates a text file with that content by using a filedialog.
    '''
    try:
        content = text_area.get(1.0, tk.END)
        with filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('.txt', '*.txt*')]) as f:
            f.write(content)
            opened_file_to_value(f.name)
    except AttributeError:
        '''
        If no file is selected
        '''
        return


def save_file():
    """
    Function that checks if there is a file in use or not. If that is the case, it just saves the content into the text file being used.
    If the user is working with a new file, it calls the save_file_as() function.
    """
    try:
        global opened_file
        if opened_file != '':
            content = text_area.get(1.0, tk.END)
            with open(opened_file, 'w') as mf:
                mf.write(content)
        else:
            save_file_as()
    except AttributeError:
        '''
        If no file is selected
        '''
        pass
    

w = tk.Tk()

# Starts Widgets creation ------------------------------------------------------------------------------------------------------------
text_area = tk.Text(w, font="Times 12", width=1280, height=720)

# Menu
main_menu = tk.Menu(w)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_file_as)
file_menu.add_command(label="Exit", command=w.quit)

# Ends Widgets creation --------------------------------------------------------------------------------------------------------------

# Starts Widgets placing  ------------------------------------------------------------------------------------------------------------
text_area.pack()
main_menu.add_cascade(label="Archivo", menu=file_menu)

# Ends Widgets placing  --------------------------------------------------------------------------------------------------------------

w.title("Bloc de notas Tkinter")
w.minsize(width=1280, height=720)
w.geometry("1280x720")
w.config(menu=main_menu)
w.mainloop()

# Para colocar el menú:
#   1. Crear el objeto tk.Menu()
#   2. Añadirlo con algún método add() [como add_cascade() si el menú mostrará opciones o add_command() si el menú ejecutará comandos].
#   3. Establecer el menú en la configuración de la ventana.
#   * Para añadir opciones al menú, se agregan menús dentro de menús.
#   * Para quitar el botón inicial del menú que muestra varios guiones y que separa el menú en una ventana independiente, se usa tearoff=0


# PARA OBTENER EL NOMBRE Y LA RUTA COMPLETA DEL ARCHIVO USADO EN LAS FUNCIONES DE filedialog:
#   Se crea un objeto tipo io.TextIOWrapper. Si en una terminal se importa la clase io y luego se usa la función dir con io.TextIOWrapper, se ven los distintos atributos
#   y métodos. EL atributo necesario es name, el cual devuelve la información mencionada como string.


# Para el trabajo con variables de estado (globales), parece ser una buena práctica hacer funciones para gestionar cambios.
# Por lo anterior, hicimos dos funciones que establecen dos valores distintos para la clave
