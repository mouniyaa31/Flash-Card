from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    df = pd.read_csv("data/learn.csv")
except FileNotFoundError:
    df1 = pd.read_csv("data/Espanol.csv")
    to_learn = df1.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")



def flip():
    canvas.itemconfig(lang_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white",  text=current_card["English"])
    canvas.itemconfig(card_bg, image=card2_img)


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text="Espanol", fill="black")
    canvas.itemconfig(word_text, text=current_card["Espanol"], fill="black")
    canvas.itemconfig(card_bg, image=card1_img)
    timer = window.after(3000, func=flip)


def wrong():
    next_card()


def right():
    to_learn.remove(current_card)
    # print(len(to_learn))
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Learn Espanol")
window.config(padx=100, pady=60, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card1_img = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(400, 263, image=card1_img)
card2_img = PhotoImage(file="images/card_back.png")
lang_text = canvas.create_text(400, 150, text="Espanol", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="spanish", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
button1 = Button(text="Start", image=wrong_img, command=next_card, highlightthickness=0)
button1.grid(column=0, row=2)
correct_img = PhotoImage(file="images/right.png")
button2 = Button(text="Reset", image=correct_img, command=right, highlightthickness=0)
button2.grid(column=1, row=2)

next_card()

window.mainloop()

