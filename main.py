from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}



try:
    data_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data_file.to_dict(orient="records")


def card_generator():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(data_dict)
    canvas.itemconfig(card_img, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")

def learn():
    data_dict.remove(card)
    print(len(data_dict))
    data_file = pandas.DataFrame(data_dict)
    data_file.to_csv("data/words_to_learn.csv", index=False)
    card_generator()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=learn)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=card_generator)
wrong_button.grid(row=1, column=0)

card_generator()
window.mainloop()
