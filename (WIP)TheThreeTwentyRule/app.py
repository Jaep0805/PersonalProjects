from threading import *
import tkinter as tk
import os
import time

start_time = 0

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()
      start_time = time.time()

   def cancel(self):
      self.thread.cancel()

   def gettime(self):
      print(time.time() - start_time)

def printer():
    print('ipsem lorem')
    notify("For Twenty seconds", "Stare!")
    

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


t = perpetualTimer(5,printer)

def startnotification():
   t.start()

def stopnotification():
   t.cancel()

def endapp():
   t.cancel()
   exit()

HEIGHT = 400
WIDTH = 700

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack() 

frame = tk.Frame(root, bg = 'gray')
frame.place(relx = 0.1, rely = 0.1, relwidth = .8, relheight = .8)

button = tk.Button(frame, text = 'Start notification', font = 30, command = startnotification)
button.place(relx = .3, rely = .5, relwidth = .2, relheight = .1)

button = tk.Button(frame, text = 'Stop notification', font = 2, command = stopnotification)
button.place(relx = .6, rely = .5, relwidth = .2, relheight = .1)

button = tk.Button(frame, text = 'Quit', font = 2, command = endapp)
button.place(relx = .3, rely = .7, relwidth = .3, relheight = .1)

label = tk.Label(frame, text = 'Rest your eyes', bg = 'gray', font = 30)
label.place(relx = .3, relwidth = .2, relheight = .2)

scale = tk.Scale(frame, orient = 'horizontal', length = 560)
scale.place(relx = 0, rely = .85)

root.mainloop()



