from tkinter import *
import random
import time


sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Flask makes web development easy and fun.",
    "Practice makes perfect.",
    "OpenAI creates advanced AI models.",
    "Typing speed tests are a great way to improve your typing skills.",
    "Consistent practice can significantly increase your typing speed.",
    "Accuracy is just as important as speed when typing.",
    "Remember to take breaks and maintain good posture while typing.",
    "Typing is an essential skill in the modern digital world.",
    "Different keyboard layouts can affect typing speed and accuracy.",
    "Touch typing involves typing without looking at the keyboard.",
    "Typing competitions can be a fun way to challenge yourself.",
    "Regular practice can help you type faster and more accurately.",
    "The journey to becoming a fast typist requires patience and dedication.",
]

BACKGROUND = "#ffffff"
FONT = ("Arial", 30, "bold")
RESULT_FONT = ("Arial", 16, "bold")
TEXT_FONT = ("Arial", 16)
BUTTON_FONT = ("Arial", 12)

word_count = 0
text = ""
time_left = 60
start_time = time.time()


# ------------------------------------------- Program --------------------------------------------
def random_sentence():
    global text
    text = random.choice(sentences).strip()
    return text



def start(event=None):
    global word_count
    entered_sentence = entry_text.get().strip()
    print(f"Entered Sentence: '{entered_sentence}'")


    if text == entered_sentence:
        word_count += len(entered_sentence.split())
        result_text.config(text=f"Word Count: {word_count}", fg="green")
        entry_text.delete(0, "end")
        random_sentence()
        random_text.config(text=text)
        wpn()

    else:
        print("No match")
        result_text.config(text="No match", fg="red")

def restart():
    global word_count, time_left
    restart_button.config(state="disabled", bg="#95a5a6")
    entry_text.config(state="normal")
    entry_text.focus()
    word_count = 0
    time_left = 60

    entry_text.delete(0, "end")
    random_text.config(text=text)
    result_text.config(text="Result shows here!", fg="black")
    update_timer()


def update_timer():
    global time_left, word_count
    if time_left > 0:
        time_left -= 1
        timer_count.config(text=f"00:{time_left:02d}")
        windows.after(1000, update_timer)

    else:
        entry_text.config(state="disabled")
        restart_button.config(state="normal", bg="#3498db")

def wpn():
    elapsed_time = (time.time() - start_time) / 60  # Calculate elapsed time in minutes
    wpm = word_count / elapsed_time if elapsed_time > 0 else 0  # Calculate WPM
    result_text.config(text=f"You typed {wpm:.2f} words per minute.", fg="blue")



random_sentence()

# ------------------------------------------- UI --------------------------------------------

windows = Tk()
windows.title("Typing Speed Test")
windows.config(padx=100, pady=50, bg=BACKGROUND)

title = Label(text="Typing speed test", font=FONT, background=BACKGROUND)
title.config(pady=20)
title.grid(column=1, row=0)

canvas = Canvas(width=800, height=400)
canvas.grid(column=1, row=1)

random_text = Label(text=f"{text}", font=TEXT_FONT, wraplength=600)
canvas.create_window(400, 60, window=random_text)

timer_count = Label(text="01:00", font=TEXT_FONT)
canvas.create_window(760, 20, window=timer_count)


entry_text = Entry(width=60, state="disabled")
canvas.create_window(380, 160, window=entry_text)
entry_text.bind("<Return>", start)

restart_button = Button(width=8, height=2, text="Start", font=BUTTON_FONT, background="#3498db", borderwidth=0,
                        command=restart)
canvas.create_window(680, 160, window=restart_button)

result_text = Label(text="Result shows here!", font=RESULT_FONT)
canvas.create_window(400, 300, window=result_text)


print(text)
print(word_count)

windows.mainloop()
