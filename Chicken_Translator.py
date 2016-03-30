#Michael Elkan
#3/27/16
from tkinter import *


class Window(Frame):

    def __init__(self, master =None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Chicken Translator")
        self.pack(fill = BOTH, expand=1)

        toOpButton = Button(self, text = "To OP Code",height = 2, command=self.toOpCode)
        toOpButton.place(x=0,y=388)

        toChickenButton = Button(self, text = "To Chicken", height = 2, command=self.toChicken)
        toChickenButton.place(x=75, y =388)

        clearButton = Button(self, text ="Clear", height = 2, command=self.clear)
        clearButton.place(x=146, y=388)      

        self.textfield = Text(self, wrap=WORD, height = 24,width = 89)
        self.textfield.place(x=0, y=0)
        

    def clear(self):
        self.master.title("Chicken Translator")
        self.textfield.delete('1.0',END)
                
    def toOpCode(self):        
        s= self.textfield.get("1.0",END)
        self.textfield.delete('1.0',END)
        self.master.title("Chicken Translator - OP CODE")
        #self.textfield.insert(END,"----------OP CODE----------\n")        
        l=[]
        st = []
        l=s.splitlines()
        counter =0
        for x in l:
            counter =0
            for c in x:
                counter= counter+1
            newc = int(((counter+1)/8))
            if newc == 0:
                self.textfield.insert(END,"exit\n")
            elif newc == 1:
                self.textfield.insert(END,"chicken\n")
            elif newc == 2:
                self.textfield.insert(END,"add\n")
            elif newc == 3:
                self.textfield.insert(END,"subtract\n")
            elif newc == 4:
                self.textfield.insert(END,"multiply\n")
            elif newc == 5:
                self.textfield.insert(END,"compare\n")
            elif newc == 6:
                self.textfield.insert(END,"load\n")
            elif newc == 7:
                self.textfield.insert(END,"store\n")
            elif newc == 8:
                self.textfield.insert(END,"jump\n")
            elif newc == 9:
                self.textfield.insert(END,"char\n")
            elif newc>=10:
                self.textfield.insert(END,"push " +str(newc-10) +"\n")
    
            

    def toChicken(self):
        o =self.textfield.get("1.0",END)
        self.textfield.delete('1.0',END)
        self.master.title("Chicken Translator - CHICKEN")
        #self.textfield.insert(END,"----------CHICKEN----------\n")
        l=[]
        l=o.splitlines()        
        for x in l:
            c = ['chicken']
            if x != '':
                if x == 'exit':
                    c=[]
                elif x == 'chicken':
                    c=c*1
                elif x == 'add':
                    c=c*2
                elif x == 'subtract':
                    c=c*3
                elif x == 'multiply':
                    c=c*4
                elif x == 'compare':
                    c=c*5
                elif x == 'load':
                    c=c*6
                elif x == 'store':
                    c=c*7
                elif x == 'jump':
                    c=c*8
                elif x == 'char':
                    c=c*9
                elif x[:4] == 'push':
                    c=c*(10+int(x[5:]))
                self.textfield.insert(END,' '.join(c)+ '\n')
            
    
            
                
root = Tk()
root.geometry("705x500")
root.resizable(width=FALSE, height=FALSE)
app = Window(root)

root.mainloop()
