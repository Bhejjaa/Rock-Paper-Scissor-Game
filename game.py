from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from random import randint
import sqlite3 as sq
# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#E6D3FF")
root.geometry('1350x600')

# # #database
# cen=sq.connect('game.db')


# c=cen.cursor()
# c.execute(''' Create table points1(
#     computerpoint int DEFAULT 1,
#     userpoint int DEFAULT 1
# )
# ''')
# c.execute('''insert into points1 values(:computerpoint, :userpoint)''',{'computerpoint':'2','userpoint':'3'})
# cen.commit()
# cen.close()



# picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#E6D3FF")
comp_label = Label(root, image=scissor_img_comp, bg="#E6D3FF")
comp_label.grid(row=1, column=0,sticky=N,pady=15)
user_label.grid(row=1, column=4,sticky=N,pady=15)

# scores
playerScore = Label(root, text=0, font=100, bg="#E6D3FF", fg='black')
computerScore = Label(root, text=0, font=100, bg="#E6D3FF", fg='black')
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root,text="USER", font='{small fonts} 15 bold',bg="#E6D3FF", fg="red")
comp_indicator = Label(root, font='{small fonts} 15 bold', text="COMPUTER",bg="#E6D3FF", fg="blue")
vs_text = Label(root, font='{small fonts} 15', text="VS",bg="#E6D3FF", fg="green")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)
vs_text.grid(row=0,column=2)
# messages
msg = Label(root, font='{small fonts} 15', bg="#E6D3FF", fg="black")
msg.grid(row=3, column=2)

# update message


def updateMessage(x):
    msg['text'] = x

# update user score


def updateUserScore():
    conn= sq.connect('game.db')
    c=conn.cursor()
    c.execute('select userpoint from points1')
    record=c.fetchall()
    print(record)
    playerScore["text"] = record[0]

    score = int(playerScore["text"])
    score += 1
    c.execute('''update points1 SET userpoint=:userpoint''',{'userpoint':score})
    conn.commit()
    conn.close

# update computer score


def updateCompScore():
    
    conn= sq.connect('game.db')
    c=conn.cursor()
    c.execute('select computerpoint from points1')
    record=c.fetchall()
    print(record)
    computerScore["text"] = record[0]

    score = int(computerScore["text"])
    score += 1
    c.execute('''update points1 SET computerpoint=:computerpoint''',{'computerpoint':score})
    conn.commit()
    conn.close
# check winner


def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


# update choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK",relief='solid',font='{small fonts}',
              bg="#FF3E4D", fg="black", command=lambda: updateChoice("rock")).grid(row=2, column=1,sticky=N)
paper = Button(root, width=20, height=2, text="PAPER",relief='solid',font='{small fonts}',
               bg="#FAD02E", fg="black", command=lambda: updateChoice("paper")).grid(row=2, column=2,sticky=N)
scissor = Button(root, width=20, height=2, text="SCISSOR",relief='solid',font='{small fonts}',
                 bg="#0ABDE3", fg="black", command=lambda: updateChoice("scissor")).grid(row=2, column=3,sticky=N)

root.mainloop()