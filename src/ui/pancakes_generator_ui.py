from PIL._tkinter_finder import tk

def user_pancakes(number: int):
    root = tk.Tk()
    root.title("Pancake Problem")
    pancake_height = 55
    title_and_button_space = 150
    height = number * pancake_height + title_and_button_space
    root.geometry(f"400x{height}")

    title_frame = tk.Frame(root)
    title_frame.pack(fill="x", pady=10)
    title = tk.Label(title_frame, text="Arrange your pancakes!", font=("Arial", 14, "bold"))
    title.pack(fill="x", pady=(30, 10))

    pancake_frame = tk.Frame(root)
    pancake_frame.pack(fill="both", expand=True, pady=10)
    __draw_user_pancakes(number, pancake_frame)

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill="x", pady=10)
    btn_done = tk.Button(btn_frame, text="Continue", width=20, height=2, command=root.destroy)
    btn_done.pack(pady=10)

def __draw_user_pancakes(number: int, parent: tk.Frame, callback=None):
    arr = list(range(1, number + 1))
    max_val = max(arr)
    selected = []

    pancake_frame = tk.Frame(parent)
    pancake_frame.pack(pady=20)

    for val in arr:
        scale = (val / max_val)
        width_chars = int(10 + scale * 30)
        btn = tk.Button(
            parent,
            text=str(val),
            width=width_chars - 5,
            height=1,
            bg="sandybrown",
            font=("Arial", 12, "bold"),
            command=lambda b=None: None
        )
        # reassign command after btn created
        btn.config(command=lambda b=btn: __on_pancake_click(b, selected, callback))
        btn.pack(pady=2)

def __on_pancake_click(btn, selected, callback):
    if btn in selected:
        return

    btn.config(bg="orange")
    selected.append(btn)

    if len(selected) == 2:
        __swap_texts(selected)
        __reset_colors(selected)

        if callback:
            callback([b["text"] for b in selected])  # optional hook

def __swap_texts(selected):
    btn1, btn2 = selected
    txt1, txt2 = btn1["text"], btn2["text"]
    btn1.config(text=txt2)
    btn2.config(text=txt1)

def __reset_colors(selected):
    for btn in selected:
        btn.config(bg="sandybrown")
    selected.clear()


