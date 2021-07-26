from tkinter import *
from tkinter import ttk

back_color = "#212121"

root = Tk()
root.configure(bg=back_color)
root.geometry("400x400")
root.title("Dashboard")

frame = LabelFrame(root, padx=50, pady=50)
frame.configure(bg=back_color)
frame.grid(column=0, row=0, padx=80, pady=80)

button = Button(frame, text="Button")
button.pack()
# mainframe = ttk.Frame(root, padding="10,10,10,10")

root.mainloop()
