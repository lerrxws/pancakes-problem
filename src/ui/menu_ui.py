from PIL._tkinter_finder import tk


def show_menu():
    root = tk.Tk()
    root.title("Pancake Problem")
    root.geometry("400x450")

    center_frame = tk.Frame(root)
    center_frame.pack(expand=True)

    title = tk.Label(center_frame, text="Welcome to the\nPancake Problem!", font=("Arial", 20, "bold"),
                     justify="center")
    title.pack(pady=10)

    img = Image.open("assets/pancake.png")
    img = img.resize((100, 100))  # adjust size
    pancake_img = ImageTk.PhotoImage(img)

    label = tk.Label(center_frame, image=pancake_img)
    label.pack(pady=20)

    btn_start = tk.Button(center_frame, text="Start", width=20, height=2)
    btn_start.pack(pady=10)

    btn_quit = tk.Button(center_frame, text="Quit", width=20, height=2, command=root.quit)
    btn_quit.pack(pady=10)

    root.mainloop()

    root.mainloop()