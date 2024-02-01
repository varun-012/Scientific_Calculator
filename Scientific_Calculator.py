from tkinter import *
import math
# import parser
import tkinter.messagebox

root = Tk()
# Title for our Frame
root.title("Scientific Calculator")
# Background colour of our frame
root.configure(background="BlanchedAlmond")
# Dimensions of our frame
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

# Gives the Frame
calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    # Function to call numbers
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    # Function for Equal to
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    # Functions for Basic Arithmetic Operations
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def mod(self):
        self.result = False
        self.current = math.modf(float(txtDisplay.get()))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def atanh(self):
        self.result = False
        self.current = math.atanh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()

# For the Grid
txtDisplay = Entry(calc, font=("arial", 20, "bold"),
                   bg="blanchedAlmond", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
# j is for Rows and k is for columns in the numberpad
for j in range(2, 5):
    for k in range(3):
        # Dimensions of individual Buttons
        btn.append(Button(calc, width=6, height=2, font=(
            "arial", 20, "bold"), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
        i += 1


# ================================Standard Calculator================================
# Buttons for specific operations, chr() = it displays the character if it's ascii value is inserted in it
# Button for Clear
btnClear = Button(calc, text=chr(67), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                  command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)
# Button for Clear All
btnClear_All = Button(calc, text=chr(67)+chr(69), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                      command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)
# Button for Squareroot
btnSq = Button(calc, text="√ ", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
               command=added_value.squared).grid(row=1, column=2, pady=1)
# Button for Addition
btnAddl = Button(calc, text="+", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                 command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)
# Button for Subtraction
btnSub = Button(calc, text="-", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)
# Button for Multiplication
btnSub = Button(calc, text="x", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)
# Button for Division
btnSub = Button(calc, text=chr(247), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)
# Button for Zero
btnZero = Button(calc, text="0", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                 command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
# Button for Dot
btnDot = Button(calc, text=".", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
# Button for Plus or Minus
btnPM = Button(calc, text=chr(177), width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
               command=added_value.mathsPM).grid(row=5, column=2, pady=1)
# Button for Equal to
btnEquals = Button(calc, text="=", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                   command=added_value.sum_of_total).grid(row=5, column=3, pady=1)


# ================================Scientific Calculator================================
# Buttons for specific operations, chr() = it displays the character if it's ascii value is inserted in it
# Button for Pi
btnPi = Button(calc, text="Pi", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
               command=added_value.Pi).grid(row=1, column=4, pady=1)
# Button for Sin
btnSin = Button(calc, text="Sin", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=added_value.sin).grid(row=1, column=7, pady=1)
# Button for Cos
btnCos = Button(calc, text="Cos", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=added_value.cos).grid(row=1, column=5, pady=1)
# Button for Tan
btnTan = Button(calc, text="Tan", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=added_value.tan).grid(row=1, column=6, pady=1)


# Button for 2Pi
btn2Pi = Button(calc, text="2Pi", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=added_value.tau).grid(row=2, column=4, pady=1)
# Button for Sinh
btnSinh = Button(calc, text="Sinh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                 command=added_value.sinh).grid(row=2, column=7, pady=1)
# Button for Cosh
btnCosh = Button(calc, text="Cosh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                 command=added_value.cosh).grid(row=2, column=5, pady=1)
# Button for Tanh
btnTanh = Button(calc, text="Tanh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                 command=added_value.tanh).grid(row=2, column=6, pady=1)


# Button for Log
btnlog = Button(calc, text="log", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=added_value.log10).grid(row=3, column=4, pady=1)
# Button for Exp
btnExp = Button(calc, text="Exp", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=added_value.exp).grid(row=3, column=5, pady=1)
# Button for Mod
btnMod = Button(calc, text="Mod", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)
# Button for E
btnE = Button(calc, text="e", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
              command=added_value.e).grid(row=3, column=7, pady=1)


# Button for Log2
btnlog2 = Button(calc, text="log2", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                 command=added_value.log2).grid(row=4, column=4, pady=1)
# Button for Deg
btndeg = Button(calc, text="deg", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                command=added_value.degrees).grid(row=4, column=5, pady=1)
# Button for acosh
btnacosh = Button(calc, text="acosh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                  command=added_value.acosh).grid(row=4, column=6, pady=1)
# Button for asinh
btnasinh = Button(calc, text="asinh", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                  command=added_value.asinh).grid(row=4, column=7, pady=1)


# Button for Log10
btnlog10 = Button(calc, text="log10", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                  command=added_value.log10).grid(row=5, column=4, pady=1)
# Button for atanh
btnatanh = Button(calc, text="log1p", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                  command=added_value.tanh).grid(row=5, column=5, pady=1)
# Button for expm1
btnexpm1 = Button(calc, text="expm1", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                  command=added_value.expm1).grid(row=5, column=6, pady=1)
# Button for gamma
btngamma = Button(calc, text="gamma", width=6, height=2, font=("arial", 20, "bold"), bd=4, bg="blanchedAlmond",
                  command=added_value.lgamma).grid(row=5, column=7, pady=1)

lblDisplay = Label(calc, text="Scientific Calculator",
                   font=("arial", 30, "bold"), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)
# =======================Menu and Function========================

# Exit Function


def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

# Scientific Function for Scientific Calculator


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")

# Standard Function for Normal Calculator


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("500x568+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
# To add a icon on top of top
menubar.add_cascade(label="File", menu=filemenu)
# To add a label inside main icon
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
# Just adds a line in between
filemenu.add_separator()
# Calling iExit Function Below
filemenu.add_command(label="Exit", command=iExit)

editmenu = Menu(menubar, tearoff=0)
# To add a icon on top of top
menubar.add_cascade(label="Edit", menu=editmenu)
# To add a label inside main icon
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
# Just adds a line in between
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
# To add a icon on top of top
menubar.add_cascade(label="Help", menu=helpmenu)
# To add a label inside main icon
helpmenu.add_command(label="View Help")

root.configure(menu=menubar)
root.mainloop()

# End of Program
# Done by Students of SRM University AP under Final Project for Python course in 3rd Semester
