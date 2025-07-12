from PIL._tkinter_finder import tk


def choose_heuristic() -> str:
    root = tk.Tk()
    root.title("Choose Algorithm")
    root.geometry("400x450")

    center_frame = tk.Frame(root)
    center_frame.pack(expand=True, pady=30)

    algo_var = tk.StringVar(value="ucs")  # Default value

    tk.Label(center_frame, text="Select algorithm to solve:", font=("Arial", 16, "bold")).pack(pady=(10, 40))

    options = [("Gap Heuristic", "gap"),
               ("Out of Place", "out_of_place"),
               ("Total Distance", "distance")]

    for text, value in options:
        tk.Radiobutton(
            center_frame,
            text=text,
            variable=algo_var,
            value=value,
            font=("Arial", 14),
            padx=10,
            pady=5,
            indicatoron=True,
            width=30,
            anchor="w"
        ).pack(anchor="w", pady=5)

    tk.Button(center_frame, text="Continue", font=("Arial", 14), width=20, height=2, command=root.quit).pack(pady=30)

    root.mainloop()
    root.destroy()

    return algo_var.get()