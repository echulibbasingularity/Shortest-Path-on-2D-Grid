
from tkinter import *
from PIL import ImageTk,Image

screen=Tk()



def move(x,y):
      Label(screen,text='voila').grid(row=x,column=y)
    
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            box_color='deep pink'
        else:
            box_color='honeydew2'

        Button(bg=box_color,padx = 20, pady= 10, border = 2,command=lambda: move(i,j)).grid(row=i,column=j, ipadx=20, ipady=20)
pic = ImageTk.PhotoImage(Image.open('Knight_icon.png').resize((80,80)))
knight = Label(image=pic,padx=20,pady=10)
knight.grid(row=0,column=0,columnspan=1)


screen.resizable(width=False,height=False)



screen.mainloop() 




