from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from os import listdir, system
textbackground = "#f5ffcf"
textcolor1 = "#8c49a3"
textcolor2 = "#4c66a8"

class EdituserFrame(Frame):
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
        label = Label(InfoFrame, text="Edit user", background=textbackground, font=("Times", 20))
        name_label = Label(InfoFrame, text="Player", background=textbackground, font=("Times", 14))
        self.p1name = StringVar(controller)
        self.p1name.set("")
        self.name = ttk.Combobox(InfoFrame, background=textbackground,
                                    textvariable=self.p1name, values=controller.names)

        self.p1name.trace('w', self.on_name_change)
        self.detailvar = StringVar("")
        detail_label = Label(InfoFrame, text="Details", background=textbackground, font=("Times", 14))
        self.details = Entry(InfoFrame, textvariable=self.detailvar, background=textbackground, font=("Times", 14))

        sound_option_list = listdir("/home/john/PycharmProjects/PongScoreboard/sounds/")
        # handles the more complicated sound selector logic
        self.sound_select = StringVar(controller)
        self.sound_select.set("")
        self.opt = ttk.Combobox(InfoFrame, textvariable=self.sound_select, values=sound_option_list)
        self.opt.config(font=('Times', 12), background=textbackground)
        sound_label = Label(InfoFrame, text="Victory sound", font=('Times', 14), background=textbackground)

        def callback(*args):
            Tk.update(controller)
            system("aplay " + "sounds/" + self.sound_select.get())
        self.sound_select.trace("w", callback)

        finish_button = Button(InfoFrame, text="Finish", bg=textbackground, font=("Times", 14),
                               command=lambda: self.controller.edit_user(self.name.get(),
                                                                        self.details.get(),
                                                                        self.opt.get()))

        cancel_button = Button(InfoFrame, text="Cancel", command=lambda: self.cancel(),
                               bg=textbackground, font=("Times", 14))

        # place everything in Infoframe
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=3)
        name_label.grid(row=1, column=0, padx=10)
        self.name.grid(row=1, column=1, padx=10)
        detail_label.grid(row=2, column=0, padx=10)
        self.details.grid(row=2, column=1, padx=10)
        sound_label.grid(row=3, column=0)
        self.opt.grid(row=3, column=1)
        finish_button.grid(row=4, column=0, pady=10, padx=10)
        cancel_button.grid(row=4, column=1, pady=10, padx=10)

    def cancel(self):
        self.controller.reset_game()

    def on_name_change(self, *args):
        name = self.p1name.get()
        user = self.controller.get_user_by_name(name)
        print(user.sound)
        print(user.detail)
        self.sound_select.set(user.sound)
        self.detailvar.set(user.detail)
        Tk.update(self.controller)





