# 'IMPORT' SECTION
import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

# 'VARIABLES' SECTION  
FILE_NAME = tkinter.NONE
 
WIDTH = 1280
HEIGHT = 720

# 'MAIN' SECTION
def new_file(): # CREATE 'NEW FILE' FUNCTION
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)
 
# CREATE 'SAVE FILE' FUNCTION
def save_file(): 
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()
 
# CREATE 'SAVE AS' FUNCTION
def save_as(): 
    out = asksaveasfile(mode = 'w', defaultextension = '.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Oops!", message="Unable to save file....")
 
# CREATE 'OPEN FILE' FUNCTION
def open_file(): 
    global FILE_NAME
    inp = askopenfile(mode = "r")
    if inp is None:
        return
    FILE_NAME = inp.name
 
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)
    
# WORKING WITH TKINTER
root = tkinter.Tk()
root.title("NPAD V 1.0")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.config(bg = "#fff")
 
text = tkinter.Text(root, width = WIDTH, height = HEIGHT, bg = "#fff", fg = "#000", font = "Arial 14")
text.pack()
 
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label = "New", command = new_file)
fileMenu.add_command(label = "Open", command = open_file)
fileMenu.add_command(label = "Save", command = save_file)
fileMenu.add_command(label = "Save As", command = save_as)
menuBar.add_cascade(label = "File", menu = fileMenu)
 
# 'END' SECTION
if __name__ == "__main__":
    root.config(menu=menuBar)
    root.mainloop()