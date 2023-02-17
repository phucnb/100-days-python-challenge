from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
import json
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password() -> str:
    """
    This function generates a random password for length of 10
    Password will include 2 symbols and 2 numbers

    Returns:
        str: a string of random password
    """
    password= []
    for _ in range(8):
        password.append(random.choice(letters))
    for _ in range(2):
        password.append(random.choice(symbols))
        password.append(random.choice(numbers))
    random.shuffle(password)     
    return ''.join(password)



window = Tk()
window.config(bg='white', padx=20, pady=20)
window.title("Password Manager")
window.eval("tk::PlaceWindow . center")

def generate_password():
    random_password = password()
    window.clipboard_clear()
    window.clipboard_append(random_password)
    password_entry.delete(0, END)
    password_entry.insert(0, random_password)

def confirm():
    if is_entry_empty():
        messagebox.showerror(title="Error", message="Enter all fields to continues")
        return
    
    password = {website_entry.get() : {
        'email' : email_entry.get(),
        'password' : password_entry.get()
    }}

    # If file exists then update first
    try:
        with open('password.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = password
    
    if website_entry.get() in data:
        is_confirm = messagebox.askokcancel(title="Confirm", message=f"Update\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it correct?")
            
    else:
        is_confirm = messagebox.askokcancel(title="Confirm", message=f"Email: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it correct?")
    if is_confirm:
        data.update(password)
        # Write into the file with newly data
        with open('password.json', 'w') as file:
            json.dump(data, file, indent=4)
        
    email_entry.delete(0, END)
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def search():
    website = website_entry.get()

    if not website:
        messagebox.showerror(title="Error", message="Enter a website to search")
        return
        
    try:
        with open('password.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError as e:
            messagebox.showerror(title="Error", message="Password file not exists")
    
    

    try:
        email = data[website]['email']
        password = data[website]['password']
        email_entry.delete(0, END)
        email_entry.insert(0, email)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        window.clipboard_clear()
        window.clipboard_append(password)
    except:
        messagebox.showerror(title="Not Found", message=f"No infomation found for website {website}")
        email_entry.delete(0, END)
        password_entry.delete(0, END)
    
def is_entry_empty():
    return True if not email_entry.get() or not website_entry.get() or not password_entry.get() else False

logo = PhotoImage(file='logo.png')
logo_width = logo.width()
logo_height = logo.height()
canvas = Canvas(window, bg='white', width=logo_width, height=logo_height, highlightthickness=0)
canvas.create_image(0, 0, image=logo, anchor=NW)
canvas.grid(column=1, row=0)

website_label = Label(bg='white', text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21, bg='white', borderwidth=0)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_lable = Label(bg='white', text="Email/Username")
email_lable.grid(column=0, row=2)
email_entry = Entry(width=39, bg='white', borderwidth=0)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "contact@phucnb.com")

password_label = Label(bg='white', text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21, bg='white', borderwidth=0)
password_entry.grid(column=1, row=3)

search_bt = Button(window, text="Search", bg='white', borderless=1, width=160, command=search)
search_bt.grid(column=2, row=1)

gen_pass_bt = Button(window, text="Generate Password", bg='white', borderless=1, command=generate_password)
gen_pass_bt.grid(column=2, row=3)

add_bt = Button(text="Add", width=360, borderless=1, command=confirm)
add_bt.grid(column=1, row=4, columnspan=2)

window.update()
window.mainloop()