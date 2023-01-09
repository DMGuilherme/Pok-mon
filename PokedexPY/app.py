from tkinter import *

root = Tk()
#canvas = Canvas(root,width=800,height= 800, bd=0,highlightthickness=0)
#canvas.pack()

root.title("Pokedex Pernambucana")

#img2 = canvas.create_image(25,25, img=img)

#botões
img = PhotoImage(file="PokedexPY/img/pokedex.png")
imgBotaoDireita = PhotoImage(file="PokedexPY/img/pokedexseta.png")

label_imagem = Label(root, image=img).pack()
botao = Button(root,image=imgBotaoDireita)
botao.place(x=550,y=550)




root.configure(background="#000")
root.geometry("850x950+850+50")
root.resizable(False,False)
root.mainloop()