import tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


import random
import math

ventana = tkinter.TK()
ventana.title("Space Invaders CR")
ventana.overrideredirect(True)
ventana.geometry(str(window.winfo_screenwidth())+"x"+str(window.winfo_screenheight()))
ventana.config(bg="black")

