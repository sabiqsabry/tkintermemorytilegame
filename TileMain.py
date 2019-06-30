# Memory Tile Game
# Sabiq Sabry
# ID no. : 2018107
# Module Leader : Mr Sudarshana Welihinda


from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import time
import threading
import tkinter.messagebox


def parttwo():
    
    class MemoryTile():

        def __init__(self, parent):
            self.parent = parent

            self.score = 0

            self.s = 0

            Label(firstFrame, text = " ").grid(row = 0)

            Label(firstFrame, text = "Memory Tile Game", fg = "white", bg = "navy", font = "Arial 15 bold").grid(row=1, sticky = W)

            Label(firstFrame, text = " ").grid(row = 2)

            Label(thirdFrame, text = " ").grid(row = 1)

            self.scoreLabel = Label(thirdFrame, text = "Score: ", fg = "white", bg = "darkslategray", font = "Arial 15 bold")
            self.scoreLabel.grid(row =2, sticky = E)

            Label(thirdFrame, text = " ").grid(row = 3)

            Label(thirdFrame, text = " ").grid(row=5, columnspan = 3)

            Label(thirdFrame, text = "Level 2", fg = "white", bg = "black", font = "Courier 12 bold").grid(row=6, columnspan = 3)

            self.timerLabel = Label(thirdFrame, text = "Countdown: ", fg = "white", bg = "deepskyblue", font = "Courier 12 bold")
            self.timerLabel.grid(row = 4, sticky = E)
            self.timer2Label = Label(thirdFrame, text = "--", fg = "white", bg = "deepskyblue", font = "Courier 12 bold")
            self.timer2Label.grid(row=4, column = 1, sticky = E)


            Label(secondFrame, text = " ").grid(column = 1)

            self.but = [[tk.Button(secondFrame, width=10, height=5, command=lambda row=row, column=column: self.choose_tile(row, column)) for column in range(4)] for row in range(4)]
            for row in range(3):
                for column in range(4):
                    self.but[row][column].grid(row=row, column=column)
            self.first = None
            self.db()
            self.stiles()
            self.parent.after(8000, self.htiles)

        def stiles(self):
            for row in range(3):
                for column in range(4):
                    self.but[row][column].config(text= self.answer[row][column], state = tk.DISABLED)

        def htiles(self):
            for row in range(3):
                for column in range(4):
                    self.but[row][column].config(text = "", state = tk.NORMAL)

        def db(self):
            self.answer = list('AAAABBBBCCCC')
            random.shuffle(self.answer)
            self.answer = [self.answer[:4], self.answer[4:8], self.answer[8:12], self.answer[12:]]

            for row in self.but:
                for button in row:
                    button.config(text='', state=tk.NORMAL)
            self.start_time = time.monotonic()


        def choose_tile(self, row, column):
            self.but[row][column].config(text=self.answer[row][column])
            self.but[row][column].config(state=tk.DISABLED)
            if not self.first:
                self.first = (row, column)
            else:
                a,b = self.first
                if self.answer[row][column] == self.answer[a][b]:
                    self.score = self.score + 20
                    self.answer[row][column] = ''
                    self.answer[a][b] = ''
                    if not any(''.join(row) for row in self.answer):
                        duration = time.monotonic() - self.start_time
                        messagebox.showinfo(title='Voila!', message='You WIN!: {:.1f}'.format(duration))
                        messagebox.showinfo(title= "Score", message="Bonus Points: " + str(count - int(duration)))
                        answerr = tkinter.messagebox.askquestion("Game Over", "Wanna play again?")
                        if answerr == "yes":
                            root.destroy()
                            partone()
                        else:
                            tEnd()
                        
                        self.parent.after(5000, self.db)
                else:
                    self.score = self.score - 5
                    self.parent.after(500, self.hide_tiles, row, column, a, b)

                self.first = None

            Label(thirdFrame, text = str(self.score), fg = "white", bg = "darkslategray", font = "Arial 15 bold").grid(row = 2, column = 1, sticky = E)

        def hide_tiles(self, x1, y1, x2, y2):
            self.but[x1][y1].config(text='', state=tk.NORMAL)
            self.but[x2][y2].config(text='', state=tk.NORMAL) 
        
    def timer():
        global count
        count=60
        for x in range(count):
            time.sleep(1)
            time_count=Label(thirdFrame,text=' '+str(count)+' ', fg = "white", bg = "deepskyblue", font = "Courier 12 bold").grid(row=4,column=1,sticky=E)

            count=count-1

            if (count==0):
                aanswer = tkinter.messagebox.askquestion("Time Up!", "Wanna play again?")
                if aanswer == "yes":
                    retryy()
                else:
                    tEnd()
            else:
                continue

    def start():
        w = threading.Thread(target = timer)
        w.daemon = True
        w.start()

    def tEnd():
        root2.destroy()
        return

    def beginStatement():
        start()
        memory_tile = MemoryTile(root2)

    def retryy():
        parttwo()

    root2 = tk.Tk()
    root2.geometry("350x600")
    root2.title("Memory Tile Game")

    beginButton = Button(root2, text = "Start", bg = "cyan", fg = "black", command = beginStatement)
    beginButton.grid()

    firstFrame = Frame(root2)
    firstFrame.grid(row = 0)

    secondFrame = Frame(root2)
    secondFrame.grid(row = 3)

    thirdFrame = Frame(root2)
    thirdFrame.grid(row=4, column = 0)

    root2.mainloop()

    

def partone():
    
    class MemoryTile():

        def __init__(self, parent):
            self.parent = parent

            self.score = 0

            self.s = 0

            Label(firstFrame, text = " ").grid(row = 0)

            Label(firstFrame, text = "Memory Tile Game", fg = "white", bg = "navy", font = "Arial 15 bold").grid(row=1, sticky = W)

            Label(firstFrame, text = " ").grid(row = 2)

            Label(thirdFrame, text = " ").grid(row = 1)

            self.scoreLabel = Label(thirdFrame, text = "Score: ", fg = "white", bg = "darkslategray", font = "Arial 15 bold")
            self.scoreLabel.grid(row =2, sticky = E)

            Label(thirdFrame, text = " ").grid(row = 3)

            Label(thirdFrame, text = " ").grid(row=5, columnspan = 3)

            Label(thirdFrame, text = "Level 1", fg = "white", bg = "black", font = "Courier 12 bold").grid(row=6)
            

            self.timerLabel = Label(thirdFrame, text = "Countdown: ", fg = "white", bg = "deepskyblue", font = "Courier 12 bold")
            self.timerLabel.grid(row = 4, sticky = E)
            self.timer2Label = Label(thirdFrame, text = "--", fg = "white", bg = "deepskyblue", font = "Courier 12 bold")
            self.timer2Label.grid(row=4, column = 1, sticky = E)


            Label(secondFrame, text = " ").grid(column = 1)

            self.but = [[tk.Button(secondFrame, width=10, height=5, command=lambda row=row, column=column: self.choose_tile(row, column)) for column in range(4)] for row in range(4)]
            for row in range(3):
                for column in range(4):
                    self.but[row][column].grid(row=row, column=column)
            self.first = None
            self.db()

        def db(self):
            self.answer = list('AAAABBBBCCCC')
            random.shuffle(self.answer)
            self.answer = [self.answer[:4], self.answer[4:8], self.answer[8:12], self.answer[12:]]

            for row in self.but:
                for button in row:
                    button.config(text='', state=tk.NORMAL)
            self.start_time = time.monotonic()


        def choose_tile(self, row, column):
            self.but[row][column].config(text=self.answer[row][column])
            self.but[row][column].config(state=tk.DISABLED)
            if not self.first:
                self.first = (row, column)
            else:
                a,b = self.first
                if self.answer[row][column] == self.answer[a][b]:
                    self.score = self.score + 20
                    self.answer[row][column] = ''
                    self.answer[a][b] = ''
                    if not any(''.join(row) for row in self.answer):
                        duration = time.monotonic() - self.start_time
                        messagebox.showinfo(title='Voila!', message='You WIN! Time: {:.1f}'.format(duration))
                        messagebox.showinfo(title= "Score", message="Bonus Points: " + str(count - int(duration)))
                        answerr = tkinter.messagebox.askquestion("Next", "Move onto the next level?")
                        if answerr == "yes":
                            movingon()
                        else:
                            tEnd()
                        
                        self.parent.after(5000, self.db)
                else:
                    self.score = self.score - 5
                    self.parent.after(500, self.hide_tiles, row, column, a, b)

                self.first = None

            Label(thirdFrame, text = str(self.score), fg = "white", bg = "darkslategray", font = "Arial 15 bold").grid(row = 2, column = 1, sticky = E)

        def hide_tiles(self, x1, y1, x2, y2):
            self.but[x1][y1].config(text='', state=tk.NORMAL)
            self.but[x2][y2].config(text='', state=tk.NORMAL) 
        
    def timer():
        global count
        count=60
        for x in range(count):
            time.sleep(1)
            time_count=Label(thirdFrame,text=' '+str(count)+' ', fg = "white", bg = "deepskyblue", font = "Courier 12 bold").grid(row=4,column=1,sticky=E)

            count=count-1

            if (count==0):
                aanswer = tkinter.messagebox.askquestion("Time Up!", "Wanna play again?")
                if aanswer == "yes":
                    retryy()
                else:
                    tEnd()
            else:
                continue

    def start():
        w = threading.Thread(target = timer)
        w.daemon = True
        w.start()

    def tEnd():
        root.destroy()
        return

    def beginStatement():
        start()
        memory_tile = MemoryTile(root)

    def retryy():
        partone()

    def movingon():
        root.destroy()
        parttwo()


    root = tk.Tk()
    root.geometry("350x600")
    root.title("Memory Tile Game")
    

    beginButton = Button(root, text = "Start", bg = "cyan", fg = "black", command = beginStatement)
    beginButton.grid()

    firstFrame = Frame(root)
    firstFrame.grid(row = 0)

    secondFrame = Frame(root)
    secondFrame.grid(row = 3)

    thirdFrame = Frame(root)
    thirdFrame.grid(row=4, column = 0)

    root.mainloop()

partone()
