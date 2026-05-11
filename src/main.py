import tkinter as tk
from tkinter import filedialog, font

root = tk.Tk()
root.title("Простой редактор")
root.geometry("800x600")
root.configure(bg="white")

text_area = tk.Text(root, wrap="word", bg="white", fg="black", font=("Arial", 12))
text_area.pack(fill="both", expand=True)

current_font = "Arial"
current_size = 12

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))

def change_font(f):
    global current_font
    current_font = f
    text_area.configure(font=(current_font, current_size))

def change_size(s):
    global current_size
    current_size = s
    text_area.configure(font=(current_font, current_size))

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Редактор", menu=edit_menu)

font_menu = tk.Menu(edit_menu, tearoff=0)
edit_menu.add_cascade(label="Шрифт", menu=font_menu)
font_menu.add_command(label="Arial", command=lambda: change_font("Arial"))
font_menu.add_command(label="Courier", command=lambda: change_font("Courier"))
font_menu.add_command(label="Times", command=lambda: change_font("Times"))
font_menu.add_command(label="Verdana", command=lambda: change_font("Verdana"))

size_menu = tk.Menu(edit_menu, tearoff=0)
edit_menu.add_cascade(label="Размер", menu=size_menu)
for sz in [8, 10, 12, 14, 16, 18, 20, 24, 28, 32]:
    size_menu.add_command(label=str(sz), command=lambda s=sz: change_size(s))

root.mainloop()