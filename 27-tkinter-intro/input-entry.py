from tkinter import Entry, Tk, Label, Button
from turtle import right

window = Tk()

window.title("Tkinter intro")

window.minsize(width=500, height=300)

# Labels
my_label = Label(text="I am a label, try to change me", font=("Arial", 14))
my_label.pack()



# Form input text
input = Entry(width=40)
input.pack()


def btn_on_click():
    global counter
    new_label_text = input.get()
    my_label.config(text=new_label_text)

# Buttons
button = Button(text="submit", command=btn_on_click)
button.pack()




window.mainloop()
