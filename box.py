from tkinter import *

root = Tk()


entry = Entry(root, width=30)
# entry.grid(row=0, column=0)
entry.pack()
entry.insert(0, "Enter your name")


def click():
    output_str = "Hello " + entry.get()
    label = Label(root, text=output_str)
    # label.grid(row=2, column=0)
    label.pack()

button = Button(root, text="Hit me", padx=60, pady=20, command=click)
# button.grid(row=1, column=0)
button.pack()



root.mainloop()
