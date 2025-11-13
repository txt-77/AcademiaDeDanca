from tkinter import *

# def mudar_pagina(pag):
#     match pag:
#         case 1:#inicial
#                return
#         case 2:#sobre nos
#                return
#         case 3:#alugueis
#                 return
#     return
root = Tk()
root.title("PlaceHolder")

#para emular o formato de um site
Header= Frame(root)
Body= Frame(root)
Footer= Frame(root)
Header.grid(row=0,column=0,sticky="ew")
Body.grid(row=1,column=0,sticky="ew")
Footer.grid(row=2,column=0,sticky="ew")

#informaçoes do topo
logo = Label(Header,text="logo")
logo.grid(row=0,column=0,sticky="w")
#logo.bind("<Button-1>", lambda: mudar_pagina(1))

#espaçamento
Label(Header,text="",width=20).grid(row=0,column=1,columnspan=2)

about = Label(Header,text="sobre nós")
about.grid(row=0,column=3)
#about.bind("<Button-1>", lambda: mudar_pagina(2))

aula = Label(Header,text="alugar aula")
aula.grid(row=0,column=4)
#aula.bind("<Button-1>", lambda: mudar_pagina(3))

#corpo (decidir oque colocar aqui)
Label(Body,text="lorem").grid(row=0,column=0)
Label(Body,text="2").grid(row=1,column=0)
Label(Body,text="3").grid(row=2,column=0)

#informaçoes extras (decidir oque colocar aqui tmb)
Label(Footer,text="1").grid(row=0,column=0)
root.mainloop()