from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_cards = {}
to_learn = {}

try:
    data = pandas.read_csv("Data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient= "records")


def next_card():
    global current_cards, flip_timer
    window.after_cancel(flip_timer)
    current_cards = random.choice(to_learn)
    canvas.itemconfig(title_card, text= "French", fill= "black")
    canvas.itemconfig(word_card, text=current_cards["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_card, text= "English", fill="white")
    canvas.itemconfig(word_card, text= current_cards["English"], fill="white")
    canvas.itemconfig(card_background, image= card_back_img)

def is_known():
    to_learn.remove(current_cards)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50 , bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,)
card_front_img = PhotoImage(file="Images/card_front.png")
card_back_img = PhotoImage(file="Images/card_back.png")
card_background = canvas.create_image(400, 263,image= card_front_img)
title_card = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text= "", font= ("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row= 0, column= 0, columnspan=2)

# buttons
cross_img = PhotoImage(file= "Images/wrong.png")
unknown_button = Button(image= cross_img , highlightthickness=0, command=next_card)
unknown_button.grid(row= 1, column= 0)

check_img = PhotoImage(file= "Images/right.png")
known_button = Button(image= check_img, highlightthickness=0, command=is_known)
known_button.grid(row= 1, column= 1)



next_card()


window.mainloop()