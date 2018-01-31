import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.minsize(width=300, height=200)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        code_default_text = tk.StringVar(root, value='Enter code here')
        self.code_textbox = tk.Entry(self, textvariable=code_default_text)
        self.code_textbox.grid()

        self.description_textbox = tk.Text(self)
        self.description_textbox.grid()

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
