import tkinter as tk
import re


def druecken(button):
    history_text = history["text"]
    display_text = display["text"]
    if button == "C":
        display.config(text="", fg="black")
        history.config(text="")
    elif button == "CE":
        if display_text:
            tokens = re.findall(r"\d+|\D", display_text)
            if tokens:
                tokens.pop()
                new_text = "".join(tokens)
                display.config(text=new_text)
    elif button == "=":
        try:
            result = eval(display_text)
            history.config(text=display_text + "=" + str(result))
            display.config(text=str(result))
            if result > 0:
                display.config(fg="green")
            elif result == 0:
                display.config(fg="black")
            else:
                display.config(fg="red")
        except Exception as e:
            display.config(text="Error", fg="red")
    else:
        display.config(text=display_text + button)
    print(f"Taste {button} gedrückt")


def keyboard(push):
    keyboard_buttons = "0123456789/*-+=C"
    if push.char in keyboard_buttons:
        druecken(push.char)
    elif push.keysym == "Return":
        druecken("=")
    elif push.keysym == "BackSpace":
        display_text = display["text"]
        display.config(text=display_text[:-1])


root = tk.Tk()
root.title("Taschenrechner")
root.geometry("400x500")
root.bind("<Key>", keyboard)
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

history = tk.Label(
    root,
    bg="dark grey",
    font=("times", 15, "italic"),
    text="",
    anchor="e",
    padx=20,
    pady=10,
)
history.grid(row=0, column=0, columnspan=4, sticky="nsew")

display = tk.Label(
    root,
    bg="light grey",
    font=("times", 28, "bold", "italic"),
    text="",
    anchor="e",
    padx=20,
    pady=20,
)
display.grid(row=1, column=0, columnspan=4, sticky="nsew")

buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    "CE",
    "C",
    "+",
    "=",
]

row = 2
column = 0
for button in buttons:
    btn = tk.Button(
        root,
        text=button,
        font=("times", 15, "bold", "italic"),
        command=lambda t=button: druecken(t),
        padx=20,
        pady=20,
    )

    if button == "=":
        btn.grid(row=row, column=0, columnspan=4, sticky="nsew")
    else:
        btn.grid(row=row, column=column, sticky="nsew")

    column += 1
    if column > 3:
        column = 0
        row += 1

root.mainloop()
