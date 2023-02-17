from tkinter import *
from tkmacosx import Button
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F48484"
RED = "#F55050"
BLUE = "#86A3B8"
YELLOW = "#E8D2A6"
WHITE = '#FFFFFF'
FONT_NAME = "Courier"

PATH = 'images/'
EXTENTION = '.png'
FOCUS = 'focus'
SECTION = 'section'
BREAK = 'break'
LONG_BREAK = 'long_break'
PAUSE = 'pause'
END = 'end'

WIDTH = 300
HEIGHT = 300
FOCUS_TIME = 1
SECOND = 59
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 30
minute_count = FOCUS_TIME
second_count = SECOND
timer = None
status = ''
second_left = 0
current_section = 0

# Setup Window
window = Tk()
window.config(width=600, height=600, background=YELLOW, padx=150, pady=150)
window.title("Pomodoro")
window.eval('tk::PlaceWindow . center') # Display window at center of screen

# Initial lists of photos
focus_photos = []
for photo in range(26):
    focus_photos.append(PhotoImage(file=f'{PATH}{FOCUS}{photo}{EXTENTION}'))
section_photos = []
for section in range(5):
    section_photos.append(PhotoImage(file=f'{PATH}{SECTION}{section}{EXTENTION}'))
short_break_photos = []
for short_break in range(301):
    short_break_photos.append(PhotoImage(file=f'{PATH}{BREAK}{short_break}{EXTENTION}'))
long_break_photos = []
for long_break in range(31):
    long_break_photos.append(PhotoImage(file=f'{PATH}{LONG_BREAK}{long_break}{EXTENTION}'))

# Set up Canvas
canvas = Canvas(window, bg=YELLOW, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack()

# Set up image objects in canvas
focus_container = canvas.create_image(0, 0, anchor=NW, image=focus_photos[0])
section_container = canvas.create_image(0, 0, anchor=NW, image=section_photos[0])
short_break_container = canvas.create_image(0, 0, anchor=NW, image=short_break_photos[0])
long_break_container = canvas.create_image(0, 0, anchor=NW, image=long_break_photos[0])
canvas.delete(long_break_container) # Hide short break and long break at the begining

# Set up time in text
time_text = canvas.create_text(150, 150, text=f'{FOCUS_TIME}:00', font=(FONT_NAME, 30), fill=BLUE)
# for photo in range(26):

def count_down(second, mode):
    # global total_min, current_min, current_second, pause_status
    global status, second_left, current_section
    min = math.floor(second / 60)
    second_count = second % 60
    if second_count < 9:
        second_count = f'0{second_count}'

    if status == PAUSE:
        return

    if mode == FOCUS:
        print(mode)
        if second > 0:
            second_left = second
            window.after(1000, count_down, second - 10, FOCUS)
            canvas.itemconfig(focus_container, image=focus_photos[25-min])
        else:
            current_section += 1
            print(current_section)
            canvas.itemconfig(section_container, image=section_photos[current_section])
            min = SHORT_BREAK_MIN if current_section < 4 else LONG_BREAK_MIN
            pause_bt.pack_forget()
            relax_bt.pack()
            skip_bt.pack()
        canvas.itemconfig(time_text, text=f'{min}:{second_count}')
        
    if mode == BREAK:
        if section > 4:
            second = LONG_BREAK_MIN * 60
            canvas.itemconfig(long_break_container, image=long_break_photos[LONG_BREAK_MIN * 60 - second])
        else:
            canvas.itemconfig(short_break_container, image=short_break_photos[SHORT_BREAK_MIN * 60 - second])
        if second > 0:
            second_left = second
            window.after(1000, count_down, second - 10, BREAK)
        else:
            start_bt.pack()
            skip_bt.pack_forget()
            canvas.itemconfig(short_break_container, image=short_break_photos[0])
        canvas.itemconfig(time_text, text=f'{min}:{second_count}')
        # canvas.itemconfig(focus_container, image=focus_photos[0])

    # if mode == PAUSE:
    #     return
    # if second > 0:
    #     window.after(1000, count_down, second - 1, mode)
    # else:
    #     total_min += 1
    #     window.after(1000, count_down, SECOND, min - 1)
    #     canvas.itemconfig(focus_container, image=focus_photos[25-min])

    # # Update image
    # canvas.itemconfig(time_text, text=f'{min}:{second}')
    # canvas.itemconfig(section_container, image=section_photos[int(total_min / 25)])

def update_image():
    canvas.itemconfig(focus_container, image=focus_photos[5])
    canvas.itemconfig(section_container, image=section_photos[2])

def start():
    # Hide all button and only display PAUSE button
    start_bt.pack_forget()
    continue_bt.pack_forget()
    end_bt.pack_forget()
    pause_bt.pack()

    # Start count time in FOCUS mode
    global status
    status = FOCUS
    count_down(second=FOCUS_TIME * 60, mode=FOCUS)

def pause():
    start_bt.pack_forget()
    continue_bt.pack()
    end_bt.pack()
    pause_bt.pack_forget()
    global status
    status = PAUSE

def end_press():
    # global pause_status
    # start_bt.pack()
    # continue_bt.pack_forget()
    # end_bt.pack_forget()
    # pause_bt.pack_forget()
    count_down(second=FOCUS_TIME * 60, mode=END)
    canvas.itemconfig(section_container, image=section_photos[0])
    canvas.itemconfig(focus_container, image=focus_photos[0])
    canvas.itemconfig(time_text, text=f'25:00')
    pause_status = False

def continue_press():
    start_bt.pack_forget()
    continue_bt.pack_forget()
    end_bt.pack_forget()
    pause_bt.pack()
    global status
    status = FOCUS
    count_down(second=second_left, mode=FOCUS)

def skip():
    skip_bt.pack_forget()
    relax_bt.pack_forget()
    start_bt.pack_forget()
    global status
    status = FOCUS
    start()

def relax():
    relax_bt.pack_forget()
    count_down(second=SHORT_BREAK_MIN * 60, mode=BREAK)

start_bt= Button(window, text='Start', bg=RED,fg=WHITE, borderless=1, width=200, height=50, font=(FONT_NAME, 25), command=start)
start_bt.pack()
continue_bt= Button(window, text='Continue', bg=RED,fg=WHITE, borderless=1, width=200, height=50, font=(FONT_NAME, 25), command=continue_press)
relax_bt= Button(window, text='Relax', bg=BLUE,fg=WHITE, borderless=1, width=200, height=50, font=(FONT_NAME, 25), command=relax)

end_bt= Button(window, text='End', bg=YELLOW,fg=RED, borderless=1, highlightthickness=1,highlightbackground=RED, width=200, height=50, font=(FONT_NAME, 25), command=end_press)
pause_bt= Button(window, text='Pause', bg=YELLOW,fg=RED, borderless=1, highlightthickness=1,highlightbackground=RED, width=200, height=50, font=(FONT_NAME, 25), command=pause)
skip_bt= Button(window, text='Skip', bg=YELLOW,fg=RED, borderless=1, highlightthickness=1,highlightbackground=RED, width=200, height=50, font=(FONT_NAME, 25), command=skip)

# continue_bt.pack()
# relax_bt.pack()
# end_bt.pack()
# pause_bt.pack()
# skip_bt.pack()


window.mainloop()

