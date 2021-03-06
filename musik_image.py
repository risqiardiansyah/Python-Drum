import pygame
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def __init__(self, parent):
	Frame.__init__(self, parent)
	self.insialisasiFile()
        
def insialisasiFile(self):
	self.file1 = 'D:/musik/drum/crash1.wav'

def musikCrash():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/crash1.wav')
	pygame.mixer.music.play()
	print('crash')
def musikHat():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/hat.wav')
	pygame.mixer.music.play()
	print('hat')
def musikKick():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/kick1.wav')
	pygame.mixer.music.play()
	print('Kick')
def musikSnare():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/snare.wav')
	pygame.mixer.music.play()
	print('snare')
def musikTom1():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/tom1.wav')
	pygame.mixer.music.play()
	print('Tom1')
def musikTom2():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/tom2.wav')
	pygame.mixer.music.play()
	print('Tom2')
def musikTom3():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/tom3.wav')
	pygame.mixer.music.play()
	print('Tom3')
def musikRide():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('./drum/ride1.wav')
	pygame.mixer.music.play()
	print('ride')


root = Tk()

crash = PhotoImage(file="./gambar/crash.png")
photo_crash = crash.subsample(5, 5) 
hat = PhotoImage(file="./gambar/hi-hat.png")
photo_hat = hat.subsample(5, 5)
snare = PhotoImage(file="./gambar/snaree.png")
photo_snare = snare.subsample(5, 5) 
kick = PhotoImage(file="./gambar/kick.png")
photo_kick = kick.subsample(5, 5)
tom1 = PhotoImage(file="./gambar/tom1.png")
photo_tom1 = tom1.subsample(5, 5)
tom2 = PhotoImage(file="./gambar/tom2.png")
photo_tom2 = tom2.subsample(5, 5)
tom3 = PhotoImage(file="./gambar/tom3.png")
photo_tom3 = tom3.subsample(5, 5)
ride = PhotoImage(file="./gambar/ride.png")
photo_ride = ride.subsample(5, 5)

Label(root, text = 'Ini Drum Gedumbrengan Marak-marak.', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 

button_crash = tk.Button(root, text="crash", image=photo_crash, compound=TOP, command=musikCrash)
button_crash.pack(side=TOP)

button_tom1 = tk.Button(root, text="tom1", image=photo_tom1, compound=BOTTOM, command=musikTom1)
button_tom1.pack(side=TOP)

button_tom2 = tk.Button(root, text="tom2", image=photo_tom2, compound=BOTTOM, command=musikTom2)
button_tom2.pack(side=TOP)

button_ride = tk.Button(root, text="ride", image=photo_ride, compound=BOTTOM, command=musikRide)
button_ride.pack(side=RIGHT)

button_tom3 = tk.Button(root, text="tom3", image=photo_tom3, compound=BOTTOM, command=musikTom3)
button_tom3.pack(side=RIGHT)

button_hat = tk.Button(root, text="hat", image=photo_hat, compound=BOTTOM, command=musikHat)
button_hat.pack(side=LEFT)

button_snare = tk.Button(root, text="snare", image=photo_snare, compound=BOTTOM, command=musikSnare)
button_snare.pack(side=LEFT)

button_kick = tk.Button(root, text="kick", image=photo_kick, compound=BOTTOM, command=musikKick)
button_kick.pack(side=BOTTOM)

def main():
    root = Tk()
    def key(event):
        if event.char=="q" :
            musikCrash()
        if event.char=="w" :
            musikTom1()
        if event.char=="e" :
            musikTom2()
        if event.char=="r" :
            musikTom3()
        if event.char=="a" :
            musikHat()
        if event.char=="s" :
            musikSnare()
        if event.char=="d" :
            musikKick()

    root.bind("<Key>", key)
    pygame.quit()
if __name__ == '__main__':
    main()

root.mainloop()
