from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageGrab


class main:

    DEFAULT_COLOR = 'black'

    def __init__(self, master):
       
        self.master = master

        self.pen_button = Button(self.master, text='Pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)
        
        self.color_button = Button(self.master, text='Color Picker', command=self.choose_color)
        self.color_button.grid(row=0, column=1)

        self.bg_color = Button(self.master, text='Change Background color', command=self.change_bg)
        self.bg_color.grid(row=0, column=2)

        self.eraser_button = Button(self.master, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.delete_button = Button(self.master, text='Clear Canvas', command=self.clear_all)
        self.delete_button.grid(row=0, column=4)

        self.save_button = Button(self.master, text='Save File', command=self.save)
        self.save_button.grid(row=0, column=5)

        self.choose_size_button = Scale(self.master, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=6)

        self.c = Canvas(self.master, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=7)

        self.setup()

    def setup(self):
        
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.color_bg = 'white'
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def clear_all(self):
        self.c.delete(ALL)

    def save(self):
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png')])
        if file:
            x = self.master.winfo_rootx() + self.c.winfo_x()
            y = self.master.winfo_rooty() + self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png')

    def choose_color(self):
        self.eraser_on = False
        color = colorchooser.askcolor(color = self.color)[1]
        if color != None:
            self.color = color
        else:
            return None

    def change_bg(self): 
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.penwidth = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.penwidth, fill=paint_color,
                               capstyle=ROUND, smooth=True, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Application')
    root.mainloop()
