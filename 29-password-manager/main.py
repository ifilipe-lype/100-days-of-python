from tkinter import Button, Entry, Tk, Canvas, PhotoImage, Label



# CONSTANTS VALUES
LOGO_IMG_PATH = 'logo.png'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg="#FFF", padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas.config(bg="#FFF", highlightthickness=0)

logo_img = PhotoImage(file=LOGO_IMG_PATH)

canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21) 
password_entry.grid(row=3, column=1)

# Buttons
gen_pwd_btn = Button(text="Generate Password", bg="white")
gen_pwd_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, bg="white")
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
