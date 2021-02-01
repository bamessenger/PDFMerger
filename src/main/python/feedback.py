import tkinter as tk
import tkinter.messagebox

class Feedback:
    def completeMsg(self):
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showinfo("Status Update", "Merge operation complete")