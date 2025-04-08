BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

current_word = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")





def next_card():
    global clock,current_word
    window.after_cancel(clock)

    current_word= random.choice(to_learn)
    canvas.itemconfig(word_in_language,text=f"{current_word["French"]}",fill="black")
    canvas.itemconfig(language,text="French",fill="black")
    canvas.itemconfig(canvas_image,image = front_img)
    clock = window.after(3000,flip_card)

def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()



def flip_card():
    canvas.itemconfig(canvas_image,image=back_img)
    canvas.itemconfig(language,text="English",fill="white")
    canvas.itemconfig(word_in_language,text=f"{current_word["English"]}",fill="white")


canvas = Canvas(width=800 , height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
clock = window.after(3000,flip_card)


# canvas.create_image(100, 100, image=back_img)
canvas.grid(column=0, row=0,columnspan=2)

language = canvas.create_text(400,160,text="",font=("Ariel",24,"italic"))
word_in_language = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,command=is_known)
right_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)
right_button.grid(column=1,row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)


next_card()


mainloop()