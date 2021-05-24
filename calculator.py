from tkinter import *

root = Tk()
root.title("Calculator")


global button_press_count
button_press_count = 0

# Function definitions of all the buttons
def button_type(num):
    global button_press_count
    my_entry.insert(button_press_count, num)
    button_press_count += 1

global s
s = 0
def button_add():
    global s
    num = int(my_entry.get())
    my_entry.delete(0, "end")
    s += num


def button_equal():
    global s
    num = int(my_entry.get())
    my_entry.delete(0, "end")
    s += num
    my_entry.insert(0, s)


def button_clear():
    my_entry.delete(0, "end")
    s = 0


my_entry = Entry(root, width=35, borderwidth=5)
my_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Creating the buttons
number_buttons_list = []
for i in range(10):
    text = str(i)
    number_buttons_list.append(Button(root, text=text, command=lambda num=i: button_type(num), padx=40, pady=20))

button_add = Button(root, text="+", command=button_add, padx=39, pady=20)
button_equal = Button(root, text="=", command=button_equal, padx=92, pady=20)
button_clear = Button(root, text="Clear", command=button_clear, padx=82, pady=20)

# Placing the buttons on grid
count = 1
for i in range(3):
    for j in range(3):
        number_buttons_list[count].grid(row=i + 1, column=j)
        count += 1

number_buttons_list[0].grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
