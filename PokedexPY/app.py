from tkinter import *

root = Tk()
#canvas = Canvas(root,width=800,height= 800, bd=0,highlightthickness=0)
#canvas.pack()

root.title("Pokedex Pernambucana")
root.configure(background="#000")
root.geometry("850x950")

img = PhotoImage(file="PokedexPY/img/pokedex1.png")
#img2 = canvas.create_image(25,25, img=img)


label_imagem = Label(root, image=img).pack()

root.mainloop()