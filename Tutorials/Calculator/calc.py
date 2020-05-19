from tkinter import*

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal,font=("Arial", 20), 
textvariable = text_Input, bd=30, insertwidth=4,
bg="powder blue", justify = "right"
).grid(columnspan=4)

cal.mainloop()