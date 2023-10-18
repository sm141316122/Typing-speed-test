from tkinter import *
import time


article = 'I am making an entry that only allows numbers to be entered. I am currently stuck on deleting the ' \
          'character just entered if it that character is not a integer. If someone will replace the the "BLANK" ' \
          'with what needs to go in there it would be a lot of help.'

root = Tk()
root.geometry("1500x800")

canvas = Canvas(height=700, bg="#222222", highlightthickness=0)

canvas_texts = {}
correct_type = True
start_x = 200
start_y = 200
start_time = 0
num = -1
game_on = True

for i in range(len(article)):
    if i % 55 == 0:
        start_x = 200
        start_y += 50
    canvas_texts[f"{i}"] = canvas.create_text(start_x, start_y, text=article[i], font=("Arial", 25), fill="#454545")
    start_x += 20

canvas.pack(fill="x")

text = ""
t = Text(font=("Arial", 20), bg="#DDDDDD", borderwidth=0)
t.pack(fill="x")


def check_text(event):
    global text, num, game_on, start_time, correct_type
    if game_on:
        if event.keycode == 16:
            pass
        elif event.keycode == 8:
            if num > -1:
                canvas.itemconfig(canvas_texts[f"{num}"], fill="#454545")
                text = text[:-1]
                num -= 1
                correct_type = True
        else:
            if num == -1:
                start_time = time.time()
            if correct_type:
                text += event.char
                num += 1
                try:
                    if text[num] == article[num]:
                        canvas.itemconfig(canvas_texts[f"{num}"], fill="white")
                        if num == len(article) - 1:
                            end_time = time.time()
                            process = round(end_time - start_time, 0)
                            game_on = False
                            canvas.create_text(0, 0, text=f"Typing time: {process} seconds", anchor=NW,
                                               font=("Arial", 20), fill="#FF6000")
                    else:
                        canvas.itemconfig(canvas_texts[f"{num}"], fill="#FF6000")
                        correct_type = False
                except IndexError:
                    canvas.itemconfig(canvas_texts[f"{num}"], fill="#FF6000")
            else:
                t.delete(1.0, END)
                t.insert(1.0, text[:-1])


t.bind("<Key>", check_text)

root.mainloop()
