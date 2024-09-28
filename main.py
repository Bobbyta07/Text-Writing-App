from tkinter import *

window = Tk()

timer_id = None


# _________________functions______________


def reset_timer(event=None):
    # set timer_id to global
    global timer_id

    # reset timer when ever user types
    if timer_id:
        window.after_cancel(timer_id)

        # set new Timer

    timer_id = window.after(5000, clear_text)


def clear_text():
    # Clears the text in the Text widget if the user is inactive for 5 seconds
    text_widget.delete("1.0", END)


def on_focus(event):
    # Clear the Text widget when focused
    text_widget.delete(1.0, END)

    # call count_words function after 2 second
    window.after(2000, count_words)


def count_words():
    # empty list
    hold_words = []
    # convert words typed in Text Widget to python list
    hold_words = text_widget.get("1.0", END).strip(", ' \n").split(' ')

    # count number of words in list and set as word_label
    word_label.config(text=f'Number of words: {len(hold_words)}')
    # call the reset timer everytime user types
    text_widget.bind("<Key>", reset_timer)

    window.after(1000, count_words)


# _____________________ GUI_________________________

window.minsize(width=500, height=500)
window.title('Text Writing App')
window.config(pady=20, padx=20)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

text_widget = Text(font=('Courier', 13, 'normal'), wrap='word')
text_widget.insert(END, 'Start Typing...')
text_widget.grid()

word_label = Label(text=f'Number of words: 0', font=('Courier', 13, 'normal'))
word_label.grid(column=0, row=1)

text_widget.bind("<FocusIn>", on_focus)

window.mainloop()
