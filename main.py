from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    lbl_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_checkmarks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_session = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    reps +=1
    if reps % 8 == 0:
        lbl_timer.config(text="Break", fg=RED)
        countdown(long_break)
    elif reps %2 == 0:
        lbl_timer.config(text="Break", fg=PINK)
        countdown(short_break)
    else:
        lbl_timer.config(text="Work", fg=GREEN)
        countdown(work_session)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minutes = int(count / 60)
    count_seconds = count % 60
    if count_seconds in range(10):
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            lbl_checkmarks.config(text=CHECKMARK*int(reps/2))


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

lbl_timer = Label(text="Timer")
lbl_timer.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
lbl_timer.grid(column=1, row=0)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(column=2, row=2)

lbl_checkmarks = Label()
lbl_checkmarks.config(fg=GREEN, bg=YELLOW)
lbl_checkmarks.grid(column=1, row=3)

window.mainloop()
