from tkinter import *

APP_FONT = ('Inter', 10)
MILE = 0.6214

w = Tk()
w.title('Kilometer to Mile Converter')
w.config(padx=50, pady=50)

def calculate(*_):
    try:
        prompt = float(input.get())
        as_mile = str(round(prompt * MILE, 2))
        answer.config(text=as_mile)
    except ValueError:
        answer.config(text='Error')

w.bind('<Return>', calculate)

input = Entry(width=10, justify=CENTER)
input.grid(column=2, row=1)
input.focus()

km_text = Label(text='Kilometers', font=APP_FONT)
km_text.grid(column=3, row=1)

equals_text = Label(text='is equal to', font=APP_FONT)
equals_text.grid(column=1, row=2)

answer = Label(text='0', font=APP_FONT)
answer.grid(column=2, row=2)

miles_text = Label(text='Miles', font=APP_FONT)
miles_text.grid(column=3, row=2)

btn = Button(text='Calculate', command=calculate)
btn.grid(column=2, row=3)

w.mainloop()