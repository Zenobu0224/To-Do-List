import customtkinter as ctk
import tkinter as tk

ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("430x600")
        self.resizable(False, False)
        self.title("To-Do List")
        self.configure(fg_color="#dcd0ff")
        self.iconbitmap('ToDoList/imgs/icon.ico')
        self.task = ctk.StringVar()

        logo = tk.PhotoImage(file='ToDoList/imgs/logo.png')

        # FRAME FOR LOGO & ICON
        top_bar_frame = ctk.CTkFrame(self, fg_color="#c2aaff", corner_radius=4, height=85)
        top_bar_frame.pack(fill="x", pady=(0,40))

        # APP TITLE AND LOGO
        ctk.CTkLabel(top_bar_frame, text="To-Do List", font=("Comic Sans MS", 30), text_color="#000000", image=logo, compound="left").place(x=15, y=18)

        # FRAME FOR ENTRY AND BUTTON(ADD TASK)
        entry_btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        entry_btn_frame.pack()

        self.task_entry = ctk.CTkEntry(entry_btn_frame, textvariable=self.task, placeholder_text="Enter Task", font=("Comic Sans MS", 20), text_color="#000000", fg_color="transparent", width=290)
        self.task_entry.pack(ipadx=8, ipady=5, side="left")

        self.add_btn = ctk.CTkButton(entry_btn_frame, text="➕", width=60, height=42, text_color="black", border_width=1, border_color="black", fg_color="#A3C4BC", hover_color="#7A9F95", command=self.add_task)
        self.add_btn.pack(side="right")

        self.task_frame = ScrFrame(self, fg_color="transparent")
        self.task_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def add_task(self):
        yaru_koto = self.task.get()

        if yaru_koto == "":
            return
        
        # DYNAMIC FRAME THAT APPEAR EVERYTIME THE USER ADD TASK
        frame = ctk.CTkFrame(self.task_frame, height=50, fg_color="#c2aaff")    #other color: creamy_matcha = A3C4BC, shinobu_purple=c2aaff
        frame.pack(fill="x", padx=5, pady=5)

        self.task_box = ctk.CTkCheckBox(frame, text=yaru_koto, font=("Comic Sans MS", 16), text_color="#000000", hover_color="#7A9F95", border_color="#1F1F1F")
        self.task_box.pack(side="left", padx=8, pady=8)

        self.remove_task_btn = ctk.CTkButton(frame, text="❌", fg_color="red", hover_color="#FF4C4C", width=40, height=35, command=lambda f=frame: f.destroy())
        self.remove_task_btn.pack(side="right", padx=8, pady=8)

        self.task.set("")


class ScrFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, scrollbar_button_color="#7A9F95", **kwargs)