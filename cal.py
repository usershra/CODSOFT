#Calculator using tkinter
from tkinter import *
#Creating main window
comp=Tk()
comp.title("Arithmetic Calculator")
comp.geometry('800x200')
def calculate():
    try:
        num1=float(conti1.get())
        num2=float(conti2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return
    op=op_var.get()
    if op =="+":
        result=num1+num2
    elif op=="-":
         result=num1-num2
    elif op=="*":
         result=num1*num2
    elif op=="/":
         if num2==0:
             result_head.config(text="cannot divide b zero")
             return
         result=num1/num2
    else:
        result_head.config(text="Please select an operation")
        return
    result_head.config(text=f"Result:{result}")
#First number label and entry
head1=Label(comp, text="Please Enter Number 1:")
head1.grid(row=0, column=0, padx=10, pady=5)
conti1=Entry(comp)
conti1.grid(row=0, column=1, padx=10, pady=5)
#Second number label and entry
head2=Label(comp, text="Please Enter Number 2:")
head2.grid(row=1, column=0, padx=10, pady=5)
conti2=Entry(comp)
conti2.grid(row=1, column=1, padx=10, pady=5)
#Operation label and radio buttons
op_var=StringVar()
op_var.set("+")
head3=Label(comp, text="Enter the operation you want to perform:")
head3.grid(row=2, column=0, padx=10, pady=5)

ops_frame=Frame(comp)
ops_frame.grid(row=2,column=1, padx=10, pady=5)
add=Radiobutton(ops_frame, text="+",variable=op_var, value="+")
add.pack(side=LEFT)
subtract=Radiobutton(ops_frame, text="-", variable=op_var, value="-")
subtract.pack(side=LEFT)
multiply=Radiobutton(ops_frame, text="*", variable=op_var, value="*")
multiply.pack(side=LEFT)
divide=Radiobutton(ops_frame, text="/", variable=op_var, value="/")
divide.pack(side=LEFT)
#Submit Button
submit_button=Button(comp, text="Calculate",command=calculate)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)
#Label to show the result
result_head=Label(comp, text="Result:")
result_head.grid(row=4, column=0, columnspan=2, pady=5)
comp.mainloop()


    