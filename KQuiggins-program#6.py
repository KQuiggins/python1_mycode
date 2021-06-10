# Kenneth Quiggins
# Program #6 Python 1

from tkinter import *

class Roof(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Roof Calculator")
        self.configure(background="cyan")
        self.grid()

        
        self._year = 0
        self._rise = 0
        self._overhang = 0


        self.box1 = IntVar()
        self.entryLength = Entry(self, width=12, textvariable=self.box1)
        self.entryLength.grid(row=0, column=0, padx=3, pady=9)

        Label(self, text="Enter Length (ft)", bg="cyan").grid(row=0, column=1, padx=3, pady=9)

        self.box2 = IntVar()
        self.entryWidth = Entry(self, width=12, textvariable=self.box2)
        self.entryWidth.grid(row=1, column=0, padx=3, pady=9)

        Label(self, text="Enter Width (ft)", bg="cyan").grid(row=1, column=1, padx=3, pady=9)

        self.box3 = IntVar()
        self.entryRise = Entry(self, width=12, textvariable=self.box3)
        self.entryRise.grid(row=2, column=0, padx=3, pady=9)

        Label(self, text="Enter rise(1-10)", bg="cyan").grid(row=2, column=1, padx=3, pady=9)

        self.eaves = BooleanVar()
        Checkbutton(self, text="add 2 feet for eaves", variable=self.eaves, bg="cyan", 
                    command=self.getOverHang).grid(row=3, columnspan=2, padx=15, pady=10)

        self.shingle = StringVar()
        self.shingle.set(None)
        Radiobutton(self, text="20 yr shingles", variable=self.shingle, value="twenty", bg="cyan",
                    command=self.getYear).grid(row=4,column=1,padx=15, pady=5)
        Radiobutton(self, text="30 yr shingles", variable=self.shingle, value="thirty", bg="cyan",
                    command=self.getYear).grid(row=4,column=0,padx=15, pady=5)

        self.b1 = Button(self, text="Calculate Total", command=self.calcPrice)
        self.b1.grid(row=5, column=0, padx=3, pady=9)

        self.b2 = Button(self, text="Clear Form", command=self.clear)
        self.b2.grid(row=5, column=1, padx=3, pady=9)

        self.box4 = StringVar()
        self.total = Entry(self, width=12, textvariable=self.box4)
        self.total.grid(row=6, column=0, padx=3, pady=9)

        Label(self, text="Estimated Total", bg="cyan").grid(row=6, column=1, padx=3, pady=9)



    def getOverHang(self):
        if self.eaves.get():
            self._overhang = 2
        else:
            self._overhang = 0



    def getYear(self):
        if self.shingle.get() == "twenty":
            self._year = 3.25
        if self.shingle.get() == "thirty":
            self._year = 3.75



    def calcPrice(self):
        
        if self.box3.get() == 1:
            self._rise = 1.003
        elif self.box3.get() == 2:
            self._rise = 1.014
        elif self.box3.get() == 3:
            self._rise = 1.031
        elif self.box3.get() == 4:
            self._rise = 1.054
        elif self.box3.get() == 5:
            self._rise = 1.082
        elif self.box3.get() == 6:
            self._rise = 1.118
        elif self.box3.get() == 7:
            self._rise = 1.158
        elif self.box3.get() == 8:
            self._rise = 1.202
        elif self.box3.get() == 9:
            self._rise = 1.250
        elif self.box3.get() == 10:
            self._rise = 1.302
        
        
            

        area = self.box1.get() * (self.box2.get() + self._overhang) * self._rise * 1.1
        total = self._year * area
        self.box4.set("${:,.2f}".format(total))

        
        
    def clear(self):
        self.box1.set(0)
        self.box2.set(0)
        self.box3.set(0)
        self.box4.set(0)
        





def main():
    Roof().mainloop()


main()

        

        

        
