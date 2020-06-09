from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from os import listdir, system
from style import textbackground


class DeleteuserFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # configure outermost frame
        self.config(bg="white")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.controller = controller

        # create canvas for background image
        canvas = Canvas(self)
        img = ImageTk.PhotoImage(Image.open("/home/john/PycharmProjects/PongScoreboard/images/pingpongblur.jpeg").resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.ANTIALIAS))
        canvas.background = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.grid(row=0, column=0, sticky='nesw')
        canvas.columnconfigure(0, weight=1)
        canvas.rowconfigure(0, weight=1)
        canvas.rowconfigure(1, weight=2)

        # create a small frame with all of the interactive widgets
        InfoFrame = Frame(canvas, highlightthickness=4)
        InfoFrame.config(highlightbackground='black', highlightcolor='black')
        InfoFrame.config(background=textbackground)
        InfoFrame.grid(row=0, column=0)
        label = Label(InfoFrame, text="Delete user", background=textbackground, font=("Times", 20))
        name_label = Label(InfoFrame, text="Player", background=textbackground, font=("Times", 14))
        p1name = StringVar(controller)
        self.name = ttk.Combobox(InfoFrame, background=textbackground,
                                    textvariable=p1name, values=controller.names)

        finish_button = Button(InfoFrame, text="Finish", bg=textbackground, font=("Times", 14),
                               command=lambda: self.controller.delete_user(self.name.get()))

        cancel_button = Button(InfoFrame, text="Cancel", command=lambda: self.cancel(),
                               bg=textbackground, font=("Times", 14))

        # place everything in Infoframe
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=3)
        name_label.grid(row=1, column=0, padx=10)
        self.name.grid(row=1, column=1, padx=10)
        finish_button.grid(row=4, column=0, padx=10, pady=10)
        cancel_button.grid(row=4, column=1, padx=10, pady=10)

    def cancel(self):
        self.controller.reset_game()




