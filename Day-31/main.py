from tkinter import *
from tkmacosx import Button
import json, random

# Color palettes
MAIN_COLOR = "#108DB9"
SECOND_COLOR = "#F4F9FB"
ACCENT_COLOR = "#0D9167"
ADD_COLOR = "#0D9167"
PRACTICE_COLOR = "#0D9167"
GOOD_COLOR = "#F4F9FB"
NORMAL_COLOR = "#F4F9FB"
BAD_COLOR = "#F4F9FB"
TOP_COLOR = "#AAE3E2"
BOTTOM_COLOR = "#D9ACF5"
WIDTH = 390
HEIGHT = 844
BUTTON_FONT = 'Helvetica 25 bold'
LABEL_FONT = 'Helvetica 15'
TOP_LABEL_FONT = 'Helvetica 40 bold'
BTT_HEIGHT = 50
LABEL_HEIGHT = 2
# Set up window
win = Tk()
win.config(width=WIDTH, height=HEIGHT)
win.title = "Vokabulary"
win.eval("tk::PlaceWindow . center")

def load_dict():
    """
    Load Dictanary Data from Json file

    Returns:
        dict: a dict of all words in dictionary
    """

    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except:
        print("No file found")

def practice():
    global first_lang_text
    random_word = random.choice(list(load_dict().items()))
    # word = {data_list : data[data_list]}
    first_lang_text['text'] = random_word[0]
    



add_bt = Button(text="ADD", bg=ACCENT_COLOR, fg=SECOND_COLOR ,borderless=1, width= 195, height=BTT_HEIGHT, font=BUTTON_FONT)
add_bt.place(x=0, y=0)
practice_bt = Button(text="PRACTICE", bg=ACCENT_COLOR, fg=SECOND_COLOR, borderless=1, width= 195,height=BTT_HEIGHT, font=BUTTON_FONT, command=practice)
practice_bt.place(x=195, y=0)
good_lbl = Label(text="GOOD", bg=GOOD_COLOR, height=2, width=14, font=LABEL_FONT, fg=MAIN_COLOR)
good_lbl.place(x=0, y =50)
normal_lbl = Label(text="NORMAL", bg=NORMAL_COLOR,height=2, width=14, font=LABEL_FONT, fg=MAIN_COLOR)
normal_lbl.place(x=130, y=50)
bad_label = Label(text="BAD", bg=BAD_COLOR, font=LABEL_FONT, width=14, height=2, fg=MAIN_COLOR)
bad_label.place(x=260, y=50)

sum_hight_of_bt_and_label = BTT_HEIGHT + (LABEL_HEIGHT*20)

top_canvas = Canvas(win, bg=MAIN_COLOR, width=WIDTH, height= (HEIGHT-sum_hight_of_bt_and_label) / 2,highlightthickness=0)
top_canvas.place(x=0, y=sum_hight_of_bt_and_label)

win.update()
bottom_canvas = Canvas(win, bg=SECOND_COLOR, width=WIDTH,height= (HEIGHT-sum_hight_of_bt_and_label) / 2, highlightthickness=0)
bottom_canvas.place(x=0, y=sum_hight_of_bt_and_label+top_canvas.winfo_height())

first_lang_lbl = Label(text="ENGLISH", font=LABEL_FONT, bg=MAIN_COLOR, fg=SECOND_COLOR)
first_lang_lbl.place(x = WIDTH / 2, y = sum_hight_of_bt_and_label + (top_canvas.winfo_height()/2) - 60, anchor="center")
first_lang_text = Label(text="aaa", font=TOP_LABEL_FONT, bg=MAIN_COLOR, fg=SECOND_COLOR)
first_lang_text.place(x= WIDTH / 2, y = sum_hight_of_bt_and_label + (top_canvas.winfo_height()/2), anchor="center")

answer_entry = Entry(font='Helvetica 40 bold', fg=MAIN_COLOR, width=10)
answer_entry.place(x= WIDTH / 2, y = sum_hight_of_bt_and_label + (top_canvas.winfo_height()*1.5), anchor="center")

second_lang_lbl = Label(text="VIETNAMESE", font=LABEL_FONT, bg=SECOND_COLOR, fg=MAIN_COLOR)
second_lang_lbl.place(x = WIDTH / 2, y = sum_hight_of_bt_and_label + top_canvas.winfo_height()*1.5 - 60, anchor="center")
second_lang_text = Label(text="XIN CHÀO", font=TOP_LABEL_FONT, bg=SECOND_COLOR, fg=MAIN_COLOR)
# first_lang_text.place(x= WIDTH / 2, y = sum_hight_of_bt_and_label + (top_canvas.winfo_height()*1.5), anchor="center")



win.update()
win.mainloop()