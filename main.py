import scientificamerican
from itertools import zip_longest
from tkinter import *
from time import strftime

bg = "#000000"
fg = "#FFFFFF"

root = Tk()
root.configure(bg=bg)
root.title("Dashboard")
root.attributes('-fullscreen', True)

news_frame = LabelFrame(root, text=" Physics ", font=('helvetica', 20), padx=10, pady=10)
news_frame.configure(bg=bg, fg=fg)
news_frame.grid(row=0, column=0, padx=50, pady=50)

article_headings = scientificamerican.get_headings()
article_dates = scientificamerican.get_dates()
article_summaries = scientificamerican.get_summaries()

count=0
for heading,date,summary in zip_longest(article_headings, article_dates, article_summaries, fillvalue=None):
    heading_label = Label(news_frame, padx=5, pady=10, text=heading, bg=bg, fg=fg, font=('helvetica', 16))
    date_label = Label(news_frame, padx=5, pady=10, text=date, bg=bg, fg=fg, font=('helvetica', 12))
    heading_label.grid(row=count, column=0, sticky='w') 
    date_label.grid(row=count, column=1, sticky='e')
    count += 1

def time_func():
    time = strftime(" %H : %M : %S ")
    clock_lbl.config(text = time)
    clock_lbl.after(1000, time_func)

clock_lbl = Label(root, font=('helvetica', 40, 'bold'), bg=bg, fg=fg, padx=30, pady=80)
clock_lbl.grid(row=0, column=2, sticky='ne')

time_func()

root.mainloop()
