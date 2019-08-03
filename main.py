import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
 
FILE_NAME = tkinter.NONE
 
 
def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)
 
 
def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()
 
 
def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Oops!", message="Unable to save file....")
 
 
def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
 
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)
 
root = tkinter.Tk()
root.title("NPAD V 1.0")
root.minsize(width=600, height=400)
root.maxsize(width=600, height=400)
root.config(bg = "#fff")
 
text = tkinter.Text(root, width=600, height=400, bg = "#fff", fg = "#000", font = "Arial 14")
text.pack()
 
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save As", command=save_as)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)
 
root.config(menu=menuBar)
root.mainloop()
