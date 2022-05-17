from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Login form')
#root.iconbitmap('')


#root.minsize() # not minimum than this
#root.maxsize() #not maximum than this

root.geometry('350x500') #fix window size
root.configure(background = "#0096DC")

img = ImageTk.PhotoImage(Image.open("images.png"))
img_label = label(root,image = img)
image_label.pack()




root.mainloop()