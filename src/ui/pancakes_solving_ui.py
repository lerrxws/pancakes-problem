from PIL._tkinter_finder import tk

def solve_ui(states: list[list[int]]):
    canvas_height = max(300, (len(states[0])-1) * 35)

    window = tk.Tk()
    window.title("Pancake Sorting Animation")
    canvas = tk.Canvas(window, width=400, height=canvas_height, bg="white")
    canvas.pack()

    def animate(index=0):
        if index < len(states):
            __draw_pancakes_solving(canvas, states[index])
            window.after(800, animate, index + 1)  # 800ms delay

    animate()
    window.mainloop()


def __draw_pancakes_solving(canvas: tk.Canvas, arr: list[int]):
    canvas.delete("all")
    arr = arr[::-1]
    max_val = max(arr) if arr else 1
    bar_height = 30
    margin = 10
    canvas_height = int(canvas['height'])

    for i, val in enumerate(arr):
        width = 30 + (val / max_val) * 300
        x0 = (400 - width) / 2
        y1 = canvas_height - margin - i * bar_height
        y0 = y1 - (bar_height - 5)
        x1 = x0 + width

        canvas.create_rectangle(x0, y0, x1, y1, fill="sandybrown")
        canvas.create_text(200, (y0 + y1) / 2, text=str(val), fill="black", font=("Arial", 12, "bold"))
