from tkinter import *

root = Tk()
root.title("Do I have a fever?")
root.geometry("600x600")

q1rb = StringVar(value="0")
q1=Label(root,text="Do you have a headache and or a sore throat?")
q1.pack()
q1r=Radiobutton(root, text="yes",variable=q1rb,value="yes")
q1r.pack()
q1r2=Radiobutton(root, text="no",variable=q1rb,value="no")
q1r2.pack()

q2rb = StringVar(value="0")
q2=Label(root,text="Is your body tempature not normal?")
q2.pack()
q2r=Radiobutton(root, text="yes",variable=q2rb,value="yes")
q2r.pack()
q2r2=Radiobutton(root, text="no",variable=q2rb,value="no")
q2r2.pack()

q3rb = StringVar(value="0")
q3=Label(root,text="Are there any redness in your eye?")
q3.pack()
q3r=Radiobutton(root, text="yes",variable=q3rb,value="yes")
q3r.pack()
q3r2=Radiobutton(root, text="no",variable=q3rb,value="no")
q3r2.pack()

def fever():
    score=0
    if q1rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    if q2rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    if q3rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    
    if score == 1:
        messagebox.showinfo(title = "Result", message = "Result: You perhaps want to visit a doctor, just to be safe.")
    elif score == 2:
        messagebox.showinfo(title = "Result", message = "Result: You should visit a doctor, that is pretty concerning.")
    elif score == 3:
        messagebox.showinfo(title ="Result", message ="Result: Go visit a doctor, now.")
    else:
        messagebox.showinfo(title = "Report", message = "You don't need to visit a doctor.")
        
button = Button(root, text="Get Results", command=fever)
button.pack()
root.mainloop()