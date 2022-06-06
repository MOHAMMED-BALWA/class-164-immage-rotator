from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog



root = Tk()
root.geometry("550x600")
root.title("IMAGE ROTATER")
root.config(background="black")

img_path=""
def openn():
    global img_path
    img_path = filedialog.askopenfilename(title="OPEN IMAGE FILE" , filetypes=(("Image files" , "*.jpg ; *.gif ; *.png ; *.jpeg " ),))
    print(img_path)
    img = ImageTk.PhotoImage(Image.open(img_path))
    label1["image"] = img
    img.close()
    

    
def r():
    global img_path
    im = Image.open(img_path)
    rotatee = im.rotate(90)
    img = ImageTk.PhotoImage(Image.open(rotatee))
    label1["image"] = img
    img.close()
    
    

    
btn1 = Button(root , text="OPEN IMAGE" , command=openn , font=("Times New Roman Greek", 13,"bold") , bg="grey" , fg= "purple")
btn1.place(relx = 0.5 , rely = 0.1 , anchor = CENTER)

btn2 = Button(root , text="ROTATE IMAGE" , command=r , font=("Times New Roman Greek", 13,"bold") , bg="purple" , fg= "orange")
btn2.place(relx = 0.5 , rely = 0.8 , anchor = CENTER)


label1 = Label(root , bg="white")
label1.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)



root.mainloop()