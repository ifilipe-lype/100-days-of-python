from cgitb import text
from ctypes import alignment
from itertools import count
from tkinter import Button, PhotoImage, Tk, Canvas, Label
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0;

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1


    if not reps % 2 == 0:
        count_down(WORK_MIN)
        title_label.config(text="Work Time", fg=GREEN)
    else:
        if reps % 8 == 0:
            title_label.config(text="Long Break Time", fg=RED)
            count_down(LONG_BREAK_MIN)
            
        else:
            title_label.config(text="Break Time", fg=PINK)
            count_down(SHORT_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro App")
window.config(bg=YELLOW, padx=100, pady=50)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check_marks.grid(column=1, row=3)


window.mainloop()