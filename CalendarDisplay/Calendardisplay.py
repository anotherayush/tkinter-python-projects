from tkinter import *
import calendar
root = Tk()
root.title("Calendar")

l= Label(root, text='Enter Year').grid(row=0,column=0,columnspan=2)
e= Entry(root,border=5)
e.grid(row=0,column=2,padx=5)
d= Label(root, text='Enter Month').grid(row=1,column=0,columnspan=2)
f= Entry(root,border=5)
f.grid(row=1,column=2,padx=5)
def click():
  cal = calendar.TextCalendar(firstweekday = 0)
  top= Tk()
  top.minsize(250, 150)
  top.title('Month')
  y= int(e.get())
  m= int(f.get())
  d= Label(top,text=cal.formatmonth(y,m), font= "Consolas 10 bold")
  d.pack()
b= Button(root, text="See Calendar",borderwidth=5,command=click)
b.grid(row=2,column=0,padx=10,pady=10,columnspan=3)
root.mainloop()