from tkinter import *
from PIL import Image, ImageTk
from style import textbackground, textcolor1, textcolor2


class BoardFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.controller = controller

        # create canvas for background image
        canvas = Canvas(self)
        img = ImageTk.PhotoImage(Image.open("/home/john/PycharmProjects/PongScoreboard/images/pingpongblur.jpeg").resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.ANTIALIAS))
        canvas.background = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.grid(row=0, column=0, sticky='nesw')
        canvas.columnconfigure(0, weight=1)
        canvas.columnconfigure(1, weight=1)
        canvas.rowconfigure(0, weight=1)
        canvas.rowconfigure(1, weight=2)

        self.bind("<Key>", self.key)

        # declare score text variables
        self.Score_txt1 = StringVar()
        self.Score_txt2 = StringVar()

        # construct frame with player 1 information
        p1Frame = Frame(canvas, highlightthickness=4)
        p1Frame.config(background=textbackground, highlightbackground=textcolor1, highlightcolor=textcolor1)
        p1Frame.grid(row=0, column=0)
        label_1 = Label(p1Frame, textvariable=self.Score_txt1, font=("Times", 100),
                        background=textbackground, foreground=textcolor1, width=3)
        player1_label = Label(p1Frame, textvariable=controller.player1, font=("Times", 50),
                              background=textbackground, foreground=textcolor1)
        player1_detail = Label(p1Frame, textvariable=controller.p1detail, font=("Times", 14),
                              background=textbackground, foreground=textcolor1)
        p1totwin_label = Label(p1Frame, textvariable=controller.p1totwin, font=("Times", 14), background=textbackground, foreground=textcolor1)
        p1recordhyphen_label = Label(p1Frame, text="-",  font=("Times", 14, "bold"), background=textbackground, foreground=textcolor1)
        p1totloss_label = Label(p1Frame, textvariable=controller.p1totloss, font=("Times", 14), background=textbackground, foreground=textcolor1)
        p1head2head_label = Label(p1Frame, textvariable=controller.p1head2head, font=("Times", 14), background=textbackground, foreground=textcolor1)
        p1record = Label(p1Frame, text="Career record", font=("Times", 14, "bold"), background=textbackground, foreground=textcolor1)
        p1head = Label(p1Frame, text="Head to Head wins", font=("Times", 14, "bold"), background=textbackground, foreground=textcolor1)
        p1headpoints = Label(p1Frame, text="Head to Head points", font=("Times", 14, "bold"), background=textbackground, foreground=textcolor1)
        p1pointsfor = Label(p1Frame, textvariable=controller.p1pointsfor, font=("Times", 14), background=textbackground, foreground=textcolor1)

        # construct frame with player2 info
        p2Frame = Frame(canvas, highlightthickness=4)
        p2Frame.config(background=textbackground, highlightbackground=textcolor2, highlightcolor=textcolor2)
        p2Frame.grid(row=0, column=1)
        label_2 = Label(p2Frame, textvariable=self.Score_txt2, font=("Times", 100),
                        background=textbackground, foreground=textcolor2, width=3)
        player2_label = Label(p2Frame, textvariable=controller.player2, font=("Times", 50),
                              background=textbackground, foreground=textcolor2)
        player2_detail = Label(p2Frame, textvariable=controller.p2detail, font=("Times", 14),
                              background=textbackground, foreground=textcolor2)
        p2totwin_label = Label(p2Frame, textvariable=controller.p2totwin, font=("Times", 14), background=textbackground, foreground=textcolor2)
        p2totloss_label = Label(p2Frame, textvariable=controller.p2totloss, font=("Times", 14), background=textbackground, foreground=textcolor2)
        p2recordhyphen_label = Label(p2Frame, text="-",  font=("Times", 14, "bold"), background=textbackground, foreground=textcolor2)
        p2head2head_label = Label(p2Frame, textvariable=controller.p2head2head, font=("Times", 14), background=textbackground, foreground=textcolor2)
        p2record = Label(p2Frame, text="Career record", font=("Times", 14, "bold"), background=textbackground, foreground=textcolor2)
        p2head = Label(p2Frame, text="Head to Head wins", font=("Times", 14, "bold"), background=textbackground, foreground=textcolor2)
        p2headpoints = Label(p2Frame, text="Head to Head points", font=("Times", 14, "bold"), background=textbackground, foreground=textcolor2)
        p2pointsfor =  Label(p2Frame, textvariable=controller.p2pointsfor, font=("Times", 14), background=textbackground, foreground=textcolor2)

        # player player 1 information in grid
        label_1.grid(row=1, column=0, columnspan=4, padx=10)
        player1_label.grid(row=2, column=0, columnspan=4, padx=10)
        player1_detail.grid(row=3, column=0, columnspan=4, pady=10, padx=10)
        p1record.grid(row=4, column=0, padx=10, sticky="e")
        p1totwin_label.grid(row=4, column=1, padx=10)
        p1recordhyphen_label.grid(row=4, column=2)
        p1totloss_label.grid(row=4, column=3, padx=10)
        p1head.grid(row=5, column=0, padx=10, sticky="e")
        p1head2head_label.grid(row=5, column=3, padx=10)
        p1headpoints.grid(row=6, column=0, padx=10, sticky="e")
        p1pointsfor.grid(row=6, column=3, padx=10)

        # player player 2 information in grid
        label_2.grid(row=1, column=0, columnspan=4, padx=10)
        player2_label.grid(row=2, column=0, columnspan=4, padx=10)
        player2_detail.grid(row=3, column=0, columnspan=4, pady=10, padx=10)
        p2record.grid(row=4, column=0, padx=10, sticky="e")
        p2totwin_label.grid(row=4, column=1, padx=10)
        p2recordhyphen_label.grid(row=4, column=2)
        p2totloss_label.grid(row=4, column=3, padx=10)
        p2head.grid(row=5, column=0, padx=10, sticky="e")
        p2head2head_label.grid(row=5, column=3, padx=10)
        p2headpoints.grid(row=6, column=0, padx=10, sticky="e")
        p2pointsfor.grid(row=6, column=3, padx=10)


        self.Score_txt1.set(controller.score1)
        self.Score_txt2.set(controller.score2)

        self.winnerstring = StringVar()

        self.winner_label = Label(canvas, textvariable=self.winnerstring,
                                  font=("Times", 50),
                                  background=textbackground)
        self.winner_label.grid(row=3, column=0, columnspan=2)
        self.winner_label.grid_remove()

        button = Button(canvas, text="Exit", command=lambda: controller.exit_game(),
                             font=("Times", 20), bg=textbackground)
        button.grid(row=4, column=0, columnspan=2, pady=10)

    def key(self, event):
        kp = str(event.char)
        if not self.controller.gameover:
            if kp.__eq__("r") and (self.controller.score1 < self.controller.points or abs(self.controller.score1 - self.controller.score2)) <= 1:
                self.controller.score1 += 1
            if kp.__eq__("f") and self.controller.score1 > 0:
                self.controller.score1 -= 1

            if kp.__eq__("u") and (self.controller.score2 < self.controller.points or abs(self.controller.score1 - self.controller.score2)) <= 1:
                self.controller.score2 += 1
            if kp.__eq__("j") and self.controller.score2 > 0:
                self.controller.score2 -= 1

            self.Score_txt1.set(self.controller.score1)
            self.Score_txt2.set(self.controller.score2)

            if self.controller.score1 >= self.controller.points and self.controller.score1 - 1 > self.controller.score2:
                self.winner_label.grid(row=3, column=0, columnspan=2)
                self.winner_label.config(foreground=textcolor1)
                self.winnerstring.set(self.controller.player1.get() + " is the winner!")
                self.controller.gameover = True
                Tk.update(self.controller)
                self.controller.playmusic(self.controller.player1.get())

            if self.controller.score2 >= self.controller.points and self.controller.score2 - 1 > self.controller.score1:
                self.winner_label.grid(row=3, column=0, columnspan=2)
                self.winner_label.config(foreground=textcolor2)
                self.winnerstring.set(self.controller.player2.get() + " is the winner!")
                self.controller.gameover = True
                Tk.update(self.controller)
                self.controller.playmusic(self.controller.player2.get())