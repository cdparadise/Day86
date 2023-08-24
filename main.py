from tkinter import *
import random


window = Tk()
window.title("Typing Speed")
window.geometry('1000x695+250+50')
window.config(padx=20, pady=10)
canvas = Canvas(height=600, width=1000)
logo_img = PhotoImage(file="basic-position.png")
canvas.create_image(500, 175, image=logo_img)
canvas.grid(row=0, column=2)

minute = 60

with open("words.py") as file:
    rand_words = file.read().split()

random.shuffle(rand_words)
to_type = rand_words[:100]
wordcount = len(to_type)

random_words = canvas.create_text(480, 480, text=f"PRESS ENTER to begin!\n\nType the words below:"
                                                 f"\n\n{' '.join(to_type)}", font=("Courier", 12, "bold"),
                                  width=900, justify="left")
text_entry = Entry(width=115, font=("courier", 10), borderwidth=0)
text_entry.grid(row=2, column=1, columnspan=2, ipadx=5, ipady=5)
text_entry.focus()
text_entry.config(state=DISABLED)

timer_label = Label(text="Time: 60")
timer_label.grid(row=0, columnspan=2, column=2, pady=5)


def reset():
    global rand_words
    global timer_label
    global minute
    global to_type
    global text_entry
    random.shuffle(rand_words)
    to_type = rand_words[:100]
    timer_label = Label(text="Time: 60")
    timer_label.grid(row=0, columnspan=2, column=2, pady=5)
    minute = 60
    text_entry.delete(0, "end")
    text_entry.focus()
    text_entry.config(state=DISABLED)
    canvas.itemconfig(random_words, text=f"PRESS ENTER to begin!\n\nType the words below:\n\n{' '.join(to_type)}",
                      font=("Courier", 12, "bold"))


reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=1, column=1, columnspan=2, pady=6)


def wpm_typing():
    global minute
    text_entry.config(state=NORMAL)
    if minute > 0:
        minute -= 1
        timer_label.config(text=f"Time: {minute}")
        timer_label.after(1000, wpm_typing)
        if minute == 0:
            text_entry.config(state=DISABLED)
            text = text_entry.get()
            chars_count = sum(len(x) for x in text)
            words_count = round(chars_count / 5)
            canvas.itemconfig(random_words, text=f'Your average Words Per Minute (WPM) is {words_count}.',
                              font=("Courier", 24, "bold"))
            window.unbind("<Return>")
            # print(f'Your average Words Per Minute (WPM) is {words_count}.')


def start_typing(event):
    global minute
    wpm_typing()


window.bind("<Return>", start_typing)


window.mainloop()
