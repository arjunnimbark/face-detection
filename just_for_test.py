import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall

# Create the window
window = tk.Tk()
window.title("FACE DETECTOR")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')

# Define the fonts and colors
title_font = font.Font(size=30, weight='bold', family='Helvetica')
btn_font = font.Font(size=20)
bg_color = '#F0F0F0'

# Define the frame for the interface
frame1 = tk.Frame(window, bg=bg_color)

# Create the title label
title_label = tk.Label(frame1, text="HUMAN DETECTION AND CROWD COUNTING", font=title_font, bg=bg_color)
title_label.grid(row=0, column=1, pady=20)

# Create the icon label
icon_image = Image.open('icons/human_detect_ic.png').resize((150, 150), Image.ANTIALIAS)
icon_photo = ImageTk.PhotoImage(icon_image)
icon_label = tk.Label(frame1, image=icon_photo, bg=bg_color)
icon_label.grid(row=1, column=1, pady=(20, 0))

# Create the buttons
btn1_image = Image.open('icons/lamp.png').resize((50,50), Image.ANTIALIAS)
btn1_photo = ImageTk.PhotoImage(btn1_image)
btn1 = tk.Button(frame1, text='Monitor', image=btn1_photo, compound='left', font=btn_font, fg='green', command=find_motion, bg=bg_color)
btn1.grid(row=2, column=0, padx=20, pady=20)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png').resize((50,50), Image.ANTIALIAS)
btn2_photo = ImageTk.PhotoImage(btn2_image)
btn2 = tk.Button(frame1, text='Rectangle', image=btn2_photo, compound='left', font=btn_font, fg='green', command=rect_noise, bg=bg_color)
btn2.grid(row=2, column=1, padx=20, pady=20)

btn3_image = Image.open('icons/security-camera.png').resize((50,50), Image.ANTIALIAS)
btn3_photo = ImageTk.PhotoImage(btn3_image)
btn3 = tk.Button(frame1, text='Noise', image=btn3_photo, compound='left', font=btn_font, fg='green', command=noise, bg=bg_color)
btn3.grid(row=2, column=2, padx=20, pady=20)