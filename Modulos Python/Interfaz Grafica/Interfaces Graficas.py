from tkinter import * 

root = Tk()
root.title("Cerbero")
root.resizable(1,1)
root.iconbitmap("Cerberus.ico")



miFrame = Frame(root)
miFrame.pack(expand=1)
miFrame.config(width=400,height=300)
miFrame.configure(cursor="pirate")
miFrame.config(bg="blue")
miFrame.config(bd="20")
miFrame.config(relief="ridge")


root.configure(cursor="boat")
root.config(bg="red")
root.config(bd="25")
root.config(relief="sunken")


root.mainloop()

