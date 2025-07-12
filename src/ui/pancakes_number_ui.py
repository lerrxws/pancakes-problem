from PIL._tkinter_finder import tk


def show_number_field(max_val: int = 10) -> int:
    root = tk.Tk()
    root.title("Pancake Problem")
    root.geometry("400x450")

    center_frame = tk.Frame(root)
    center_frame.pack(expand=True)

    number_var = tk.IntVar(value=2)
    label_var = tk.StringVar(value="2")

    tk.Label(center_frame, text="Enter number of pancakes!", font=("Arial", 20, "bold")).pack(pady=10)
    tk.Label(center_frame, textvariable=label_var, font=("Arial", 30, "bold")).pack(pady=10)

    tk.Scale(
        center_frame,
        from_=2,
        to=max_val,
        orient="horizontal",
        length=300,
        variable=number_var,
        label="Pancakes",
        command=lambda val: label_var.set(val)
    ).pack(pady=10)

    tk.Button(center_frame
              , text="Continue", width=20, height=2, command=root.quit).pack(pady=10)

    root.mainloop()
    root.destroy()
    return number_var.get()