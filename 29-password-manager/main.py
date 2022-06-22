from tkinter import Tk, Canvas, PhotoImage



# CONSTANTS VALUES
LOGO_IMG_PATH = 'logo.png'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="#FFF", padx=20, pady=20)
window.minsize(width=540, height=620)


canvas = Canvas(width=200, height=200)
canvas.config(bg="#FFF", highlightthickness=0)

logo_img = PhotoImage(file=LOGO_IMG_PATH)

canvas.create_image(100, 100, image=logo_img)

canvas.pack()

window.mainloop()
