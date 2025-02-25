import tkinter

m = tkinter.Tk()

#Widgets are added here

m.title("Cossita")

#l = tkinter.Label(m, text="Hello world!")
#l.pack()

#b = tkinter.Button(m, text="Stop", command=m.destroy, width=25)
#b.pack()

#fn_label = tkinter.Label(m, text="First name: ")
#fn_label.grid(row=0)
#fn_label = tkinter.Label(m, text="Last name:").grid(row=1)
#fn_input = tkinter.Entry(m).grid(row=0, column=1)
#fn_input = tkinter.Entry(m).grid(row=1, column=1)

#male = tkinter.IntVar()
#tkinter.Checkbutton(m, text="Male", variable=male).grid(row=3, sticky=tkinter.W)
#female = tkinter.IntVar()
#tkinter.Checkbutton(m, text="Female", variable=female).grid(row=4, sticky=tkinter.W)

#Radio Buttons
#group= tkinter.IntVar()
#tkinter.Radiobutton(m, text="A", variable=group, value="A").grid(row=6, sticky=tkinter.W)
#tkinter.Radiobutton(m, text="B", variable=group, value="B").grid(row=7, sticky=tkinter.W)
#tkinter.Radiobutton(m, text="C", variable=group, value="C").grid(row=8, sticky=tkinter.W)

#List Box
#lb = tkinter.Listbox()
#lb.insert(1, "Python")
#lb.insert(2, "HTML")
#lb.insert(3, "CSS")
#lb.insert(4, "Javascript")
#lb.pack()b 

#Scrollbar
scrollbar = tkinter.Scrollbar(m)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
giant_list = tkinter.Listbox(m, yscrollcommand=scrollbar.set)

for line in range(100):
    giant_list.insert(tkinter.END, "This is line number" + str{line})
    
giant_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

#Menu
menu1= tkinter.Menu(m)
m.config(menu=menu1)
filemenu= tkinter.Menu(menu1)
menu1.add_cascade(label = "File", menu=filemenu)
filemenu.add_cascade(label="New")

m.mainloop()