#A simple Rock, Paper, Scissors game with UI

from tkinter import *
import random

app = Tk()
app.geometry('500x500')
app.title('Rock, Paper, Scissors')

win = 0
lose = 0

label = Label(app, text='Choose...')
label.pack()
win_label = Label(app, text='Win: '+str(win))
win_label.pack()
lose_label = Label(app, text='Lose: '+str(lose))
lose_label.pack()

choice = ['Rock', 'Paper', 'Scissors']


def battle(pc_choice):
    global win
    global lose
    enemy = ''
    random_num =  random.randint(0, 2)
    enemy = choice[random_num]
    if pc_choice == enemy:
        label.configure(text="It's a draw!")
    elif enemy == choice[0]:
        if pc_choice == choice[1]:
            label.configure(text='You WIN!')
            win = win + 1
            win_label.configure(text='Win: '+str(win))
        elif pc_choice == choice[2]:
            label.configure(text='You lose :(')
            lose = lose + 1
            lose_label.configure(text='Lose: '+str(lose))
    elif enemy == choice[1]:
        if pc_choice == choice[2]:
            label.configure(text='You WIN!')
            win = win + 1
            win_label.configure(text='Win: '+str(win))
        elif pc_choice == choice[0]:
            label.configure(text='You lose :(')
            lose = lose + 1
            lose_label.configure(text='Lose: '+str(lose))
    elif enemy == choice[2]:
        if pc_choice == choice[0]:
            label.configure(text='You WIN!')
            win = win + 1
            win_label.configure(text='Win: '+str(win))
        elif pc_choice == choice[1]:
            label.configure(text='You lose :(')
            lose = lose + 1
            lose_label.configure(text='Lose: '+str(lose))

rock = Button(app, text='Rock', command=lambda:battle(choice[0]))
rock.pack()
paper = Button(app, text='Paper', command=lambda:battle(choice[1]))
paper.pack()
scissors = Button(app, text='Scissors', command=lambda:battle(choice[2]))
scissors.pack()


app.mainloop()