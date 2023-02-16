from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(background='white', padx=20, pady=20)
window.eval('tk::PlaceWindow . center')




#label
input = Entry(width=10)
input.insert(0, string="0")
input.grid(column=2, row=1)

label_1 = Label(text='Miles')
label_1.config(background='white')
label_1.grid(column=3, row=1)

label_2 = Label(text='is equal to')
label_2.config(background='white', anchor='s')
label_2.grid(column=1, row=2)

label_3 = Label(text='0')
label_3.config(background='white')
label_3.grid(column=2, row=2)

def calculate():
    label_3['text'] = str(round(int(input.get()) * 1.60934, 5)) if radio_state.get() == 2 else str(round(int(input.get()) / 1.60934, 5))

label_4 = Label(text='Km')
label_4.config(background='white', anchor='s')
label_4.grid(column=3, row=2)

calculate_bt = Button(text='Calculate', highlightbackground='white', command=calculate)
calculate_bt.grid(column=2, row=3)

#Radiobutton
def radio_used():
    if radio_state.get() == 1:
        label_1['text'] = "Km"
        label_4['text'] = "Mile"

    else:
        label_4['text'] = "Km"
        label_1['text'] = "Mile"
    label_3['text'] = str(round(int(input.get()) * 1.60934, 5)) if radio_state.get() == 2 else str(round(int(input.get()) / 1.60934, 5))

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Km to Mile", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Mile to Km", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=4)
radiobutton2.grid(column=2, row=4)


window.mainloop()













