import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("HesapMakinesi-Enes Zengin")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_630=tk.Button(root)
        GButton_630["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_630["font"] = ft
        GButton_630["fg"] = "#000000"
        GButton_630["justify"] = "center"
        GButton_630["text"] = "+"
        GButton_630.place(x=130,y=290,width=30,height=25)
        GButton_630["command"] = self.GButton_630_command

        GButton_181=tk.Button(root)
        GButton_181["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_181["font"] = ft
        GButton_181["fg"] = "#000000"
        GButton_181["justify"] = "center"
        GButton_181["text"] = "-"
        GButton_181.place(x=230,y=290,width=30,height=25)
        GButton_181["command"] = self.GButton_181_command

        GButton_693=tk.Button(root)
        GButton_693["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_693["font"] = ft
        GButton_693["fg"] = "#000000"
        GButton_693["justify"] = "center"
        GButton_693["text"] = "*"
        GButton_693.place(x=320,y=290,width=30,height=25)
        GButton_693["command"] = self.GButton_693_command

        GButton_902=tk.Button(root)
        GButton_902["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_902["font"] = ft
        GButton_902["fg"] = "#000000"
        GButton_902["justify"] = "center"
        GButton_902["text"] = "/"
        GButton_902.place(x=420,y=290,width=30,height=25)
        GButton_902["command"] = self.GButton_902_command

        GLineEdit_573=tk.Entry(root)
        GLineEdit_573["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_573["font"] = ft
        GLineEdit_573["fg"] = "#333333"
        GLineEdit_573["justify"] = "center"
        GLineEdit_573["text"] = "Rakam1"
        GLineEdit_573.place(x=130,y=130,width=70,height=25)

        GLineEdit_133=tk.Entry(root)
        GLineEdit_133["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_133["font"] = ft
        GLineEdit_133["fg"] = "#333333"
        GLineEdit_133["justify"] = "center"
        GLineEdit_133["text"] = "Rakam2"
        GLineEdit_133.place(x=220,y=130,width=70,height=25)

        GLineEdit_437=tk.Entry(root)
        GLineEdit_437["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_437["font"] = ft
        GLineEdit_437["fg"] = "#333333"
        GLineEdit_437["justify"] = "center"
        GLineEdit_437["text"] = "Sonuc"
        GLineEdit_437.place(x=310,y=130,width=70,height=25)

    def GButton_630_command(self):
        print("toplandi")


    def GButton_181_command(self):
        print("cikarildi")


    def GButton_693_command(self):
        print("carpildi")


    def GButton_902_command(self):
        print("bolundu")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textboxyazilar1 = tk.StringVar()
    textboxyazilar2 = tk.StringVar()
    textboxyazilar3 = tk.StringVar()

    root.mainloop()


