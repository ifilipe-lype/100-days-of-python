from tkinter import Tk, Label, Button

window = Tk()

window.title("Tkinter intro")

window.minsize(width=500, height=300)

# Labels
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

counter = 0

def btn_on_click():
    global counter

    counter += 1
    my_label.config(text=f"I got clicked {counter} time{'s' if counter > 1 else ''} !")

# Buttons
button = Button(text="Click me", command=btn_on_click)
button.pack()




window.mainloop()
