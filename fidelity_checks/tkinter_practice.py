__author__ = 'ekahn'
__project__ = 'fidelity_checks'

from tkinter import *

master = Tk()
e = Entry(master)
e.pack()
mainloop()
s = e.get()
print(s)

'''

This snippet opened a dialog box, but I couldn't really work with it.

top = Tk("hello world")
L1 = Label(top,text='User Name')
L1.pack(side = LEFT)
E1 = Entry(top, bd=5)

E1.pack(side = LEFT)

top.mainloop()
'''
