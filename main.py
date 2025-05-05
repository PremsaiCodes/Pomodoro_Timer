import tkinter
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    label.config(text='Timer')
    canvas.itemconfig(timer_text, text= '00:00')
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    mark = ''
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_sec)
        label.config(text='LONG BREAK', fg=RED)
        reset_timer()
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        label.config(text='SHORT BREAK', fg=PINK)
    else:
        count_down(work_sec)
        label.config(text='WORK', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(REPS/2)):
            mark += '✓'
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

label = Label(text='Timer', font=(FONT_NAME, 25, 'bold'), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(103, 132, text="00:00", fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer, highlightthickness=-10)
reset.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'bold'), highlightthickness=-10)
checkmark.grid(column=1, row=3)

window.mainloop()
