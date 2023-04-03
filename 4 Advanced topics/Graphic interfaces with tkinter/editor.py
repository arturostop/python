from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" # Contain the route of a file

def new():
	global ruta
	mensaje.set("New file")
	ruta = ""
	texto.delete(1.0, 'end')
	root.title("Notepad ◕ ‿ ◕")

def abrir():
	global ruta
	mensaje.set("Open file")
	ruta = FileDialog.askopenfilename(
		initialdir='.',
		filetype=(("Text files", "*.txt"),),
		title="Open text file")

	if ruta != "":
		file = open(ruta, 'r')
		content = file.read()
		texto.delete(1.0, 'end')
		texto.insert('insert', content)
		file.close()
		root.title(ruta + " - my Notepad")


def save():
	mensaje.set("Save file")
	if ruta != "":
		content = texto.get(1.0, 'end-1c')
		file = open(ruta,'w+')
		file.write(content)
		file.close()
		mensaje.set("File saved")
	else:
		save_as()

def save_as():
	global ruta
	mensaje.set("Save as...")
	file = FileDialog.asksaveasfile(title="Save file", mode="w", defaultextension=".txt")
	if file is not None:
		ruta = file.name
		content = texto.get(1.0, 'end-1c')
		file = open(ruta,'w+')
		file.write(content)
		file.close()
		mensaje.set("File saved")
	else:
		mensaje.set("Not saved...")
		ruta = ""



# Configuracion de la raiz
root = Tk()
root.title("Notepad ◕ ‿ ◕")


# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open...", command=abrir)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")

# caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# monitor inferior
mensaje = StringVar()
mensaje.set("Welcome to Notepad")
monitor = Label(root,textvar=mensaje, justify='left')
monitor.pack(side='left')


root.config(menu=menubar)
# Bucle de la aplicación
root.mainloop()