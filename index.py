from tkinter import *

root = Tk()
root.title("PlaceHolder")

Header= Frame(root)
Body= Frame(root)
Footer= Frame(root)
Header.grid(row=0,column=0,sticky="ew")
Body.grid(row=1,column=0,sticky="ew")
Footer.grid(row=2,column=0,sticky="ew")

Label(Header,text="1").grid(row=0,column=0,sticky="w")
Label(Header,text="",width=20).grid(row=0,column=1,columnspan=2)
Label(Header,text="2").grid(row=0,column=3)
Label(Header,text="3").grid(row=0,column=4)

Label(Body,text="1").grid(row=0,column=0)
Label(Body,text="2").grid(row=1,column=0)
Label(Body,text="3").grid(row=2,column=0)

Label(Footer,text="1").grid(row=0,column=0)
root.mainloop()