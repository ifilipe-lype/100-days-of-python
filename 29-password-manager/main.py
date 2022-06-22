from tkinter import END, Button, Entry, Tk, Canvas, PhotoImage, Label, messagebox
from turtle import tilt


# CONSTANTS VALUES
LOGO_IMG_PATH = 'logo.png'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please make sure you haven't left any fields empty.")
        return

    should_save = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save ?"
    )

    if should_save:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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

add_btn = Button(text="Add", width=36, bg="white", command=save)
add_btn.grid(row=4, column=1, columnspan=2)

website_entry.focus()

window.mainloop()
