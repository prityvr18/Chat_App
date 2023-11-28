from tkinter import *

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END)

root = Tk()

entry = Entry()
entry.pack(side = BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root,text="send",command = lambda: send(listbox,entry))
button.pack(side = BOTTOM)

root.mainloop()
