import tkinter as tk

root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry("900x700")
root.configure(bg="white")

text_area = tk.Text(root, 
                    wrap="word", 
                    bg="white", 
                    fg="black", 
                    font=("Arial", 12),
                    padx=15, 
                    pady=15,
                    undo=True)

text_area.pack(fill="both", expand=True)

root.mainloop()