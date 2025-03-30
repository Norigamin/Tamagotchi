from tkinter import *
from PIL import Image, ImageTk

class AnimatedLabel(Label):
    def __init__(self, master, filename):
        self.frames = []
        gif = Image.open(filename)
        frames = gif.n_frames
        for frame in range(frames):
            gif.seek(frame)
            self.frames.append(ImageTk.PhotoImage(gif.copy()))

        super().__init__(master)
        self.delay = gif.info['duration']
        self.idx = 0
        self.cancel_id = None
        self.animate()

    def animate(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel_id = self.after(self.delay, self.animate)