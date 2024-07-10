from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1130x655")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 655,
    width = 1130,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    366.0, 327.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 732, y = 441,
    width = 397,
    height = 102)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 732, y = 553,
    width = 197,
    height = 102)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 932, y = 553,
    width = 197,
    height = 102)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 732, y = 348,
    width = 397,
    height = 48)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    931.5, 171.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 732, y = 0,
    width = 399,
    height = 340)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    932.5, 418.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 734, y = 403,
    width = 397,
    height = 29)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    502.0, 592.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 288, y = 577,
    width = 428,
    height = 29)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    502.0, 542.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 288, y = 527,
    width = 428,
    height = 29)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    502.0, 492.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry4.place(
    x = 288, y = 477,
    width = 428,
    height = 29)

window.resizable(False, False)
window.mainloop()
