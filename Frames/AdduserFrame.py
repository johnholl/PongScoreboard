from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from os import listdir, system
from style import textbackground


class AdduserFrame(Frame):
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
        label = Label(InfoFrame, text="New user information", background=textbackground, font=("Times", 20))
        name_label = Label(InfoFrame, text="Name", background=textbackground, font=("Times", 14))
        self.name = Entry(InfoFrame, background=textbackground, font=("Times", 14))
        detail_label = Label(InfoFrame, text="Details", background=textbackground, font=("Times", 14))
        self.details = Entry(InfoFrame, background=textbackground, font=("Times", 14))
        sound_option_list = listdir("/home/john/PycharmProjects/PongScoreboard/sounds/")
        # handles the more complicated sound selector logic
        sound_select = StringVar(controller)
        sound_select.set("")
        self.opt = ttk.Combobox(InfoFrame, textvariable=sound_select, values=sound_option_list)
        self.opt.config(font=('Times', 12), background=textbackground)
        sound_label = Label(InfoFrame, text="Victory sound", font=('Times', 14), background=textbackground)

        def callback(*args):
            Tk.update(controller)
            system("aplay " + "sounds/" + sound_select.get())
        sound_select.trace("w", callback)

        finish_button = Button(InfoFrame, text="Finish",  bg=textbackground, font=("Times", 14),
                               command=lambda: self.controller.add_user(self.name.get(),
                                                                        self.details.get(),
                                                                        self.opt.get()))

        cancel_button = Button(InfoFrame, text="Cancel", command=lambda: self.cancel(),
                                bg = textbackground, font = ("Times", 14))

        # place everything in Infoframe
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=3)
        name_label.grid(row=1, column=0, padx=10)
        self.name.grid(row=1, column=1, padx=10)
        detail_label.grid(row=2, column=0, padx=10)
        self.details.grid(row=2, column=1, padx=10)
        sound_label.grid(row=3, column=0)
        self.opt.grid(row=3, column=1)
        finish_button.grid(row=4, column=0, padx=10, pady=10)
        cancel_button.grid(row=4, column=1, padx=10, pady=10)

    def cancel(self):
        self.controller.reset_game()




