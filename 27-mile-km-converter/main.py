from tkinter import Tk, Button, Entry, Label


# window setup

window = Tk()
window.title("Miles to Kilometers converter")
window.config(padx=40, pady=40)

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = miles * 1.609
        kilometer_result_label.config(text=f"{km}")
    except:
        kilometer_result_label.config(text=f"{miles_input.get()} is not valid miles value!")

# Text input
miles_input = Entry()

# Labels
miles_label = Label(text="Miles")
is_equal_label = Label(text="is equal to")
kilometer_result_label = Label(text="0")
kilometer_label = Label(text="Km")

calc_button = Button(text="Calculate", command=miles_to_km)

# Placing widgets on screens

miles_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
kilometer_result_label.grid(column=1, row=1)
kilometer_label.grid(column=2, row=1)
calc_button.grid(column=1, row=2)


window.mainloop()
