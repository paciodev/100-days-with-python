from tkinter import *

window = Tk()
window.title('Cool GUI App')
window.minsize(500, 300)
window.config(padx=20, pady=20)

def btn_clicked():
    new_title = input.get()
    window.title(new_title)
    
    input.delete(0, 'end')


welcome_message = Label(text='Welcome in the app', font=('Inter', 24, 'bold'))
welcome_message.grid(column=1, row=1)
welcome_message.config(padx=50, pady=50)
# welcome_message.pack(side='bottom')
# welcome_message.pack(expand=True)

# welcome_message['text'] = 'New text'
# welcome_message.config(text='New text')

button = Button(text='Click me!', command=btn_clicked)
button.grid(column=2, row=2)

button = Button(text='New button')
button.grid(column=3, row=1)

input = Entry()
input.grid(column=4, row=3)
input.focus()

window.mainloop()