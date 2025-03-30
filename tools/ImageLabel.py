from tkinter import *

class ImageLabel(Label):
    def __init__(self, master, filename):
        self.image = PhotoImage(file=filename)
        super().__init__(master, image=self.image)