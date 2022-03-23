from tkinter import *
from PIL import Image, ImageTk
import random

root=Tk()

root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(background="seashell2")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player_1 = Label(root, text="Player 1", bg="RosyBrown1", fg="maroon")
player_1.place(relx=0.1, rely=0.2, anchor=CENTER)

player_2 = Label(root, text="Player 2", bg="maroon", fg="RosyBrown1")
player_2.place(relx=0.9, rely=0.2, anchor=CENTER)


player_1_score_label = Label(root, text="", bg="maroon", fg="RosyBrown1")
player_1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player_2_score_label = Label(root, text="", bg="RosyBrown1", fg="maroon")
player_2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)

winner_label = Label(root, text="The winner is : ", bg="chocolate", fg="white")
winner_label.place(relx=0.5, rely=0.5, anchor=CENTER)

player_1_score=0

def player_1() :
    global player_1_score
    random_no = random.randint(1, 6)
    winner_label["text"] = "Player one's random number is " + str(random_no)
    player_1_score = player_1_score + random_no
    player_1_score_label["text"] = str(player_1_score)

player_1_button = Button(root, image=img, command = player_1)
player_1_button.place(relx=0.1, rely=0.6, anchor=CENTER)































player_2_score = 0

def player_2() :
    global player_2_score
    random_no_2 = random.randint(1,6)
    winner_label["text"] = "Player Two's random number is " + str(random_no_2)
    player_2_score = player_2_score + random_no_2
    player_2_score_label["text"] = str(player_2_score)

player_2_button = Button(root, image=img, command=player_2)
player_2_button.place(relx=0.9, rely=0.6, anchor=CENTER)

root.mainloop()