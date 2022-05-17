from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
def handle_login() :
    email=email_input.get()
    password = pas_input.get()

    if email == 'kmonit827@gmail.com' and password =="1234" :
        messagebox.showinfo("Welcome")
    else:
        messagebox.showerror('Error','Login Failed')


root = Tk()
root.title('Login form')
#root.iconbitmap('')


#root.minsize() # not minimum than this
#root.maxsize() #not maximum than this

root.geometry('350x500') #fix window size
root.configure(background = "#0096DC")


img = Image.open("images.png")
resized_img = img.resize((100,100))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image = img)
img_label.pack(pady =(10,10))
text_label = Label(root,text = "Twitter",fg = "white",bg ="#0096DC")
text_label.pack()

email_label = Label(root,text ="Enter E-mail",fg ="white",bg="#0096DC")
email_label.pack(pady =(20,5))
email_label.config(font=('verdana',12))

email_input =Entry(root,width = 50)
email_input.pack(ipady =6, pady =(1,15))

pas_label = Label(root,text ="Enter Password",fg ="white",bg="#0096DC")
pas_label.pack(pady =(20,5))
pas_label.config(font=('verdana',12))


pas_input =Entry(root,width = 50)
pas_input.pack(ipady =6, pady =(1,15))

login_btn = Button(root,text='Login',bg ='white',fg = 'black',width =30,command = handle_login)
login_btn.pack(pady=(10,20))

root.mainloop()