import glob
from tkinter import *

def findmix(rawmix):
    mixRegex = re.compile(r'3\d{7}')
    extractedMixLst = mixRegex.findall(rawmix)
    return extractedMixLst

def all(event=None):
    pn_raw = e1_value.get()
    #pn_raw = t1_value.get()
    print(pn_raw)
    t2.insert(END, str(pn_raw))
    pn_l = findmix(pn_raw)
    #path = '\\'+'\\vcatsvcg\\Imagefiles\\'
    path = '\\'+'\\vcatsvcg.gen.volvocars.net\\Imagefiles\\'


    for pt in pn_l:
        pn_in = findmix(pt)[0]
        pn = pn_in[:5] + '.' + pn_in[-3:]
        res = (glob.glob(path + pn))
        if res != []:
            txt1 = pn_in + ' on server\n'
            t1.insert(END, txt1)
        else:
            txt2 = pn_in + " not on server\n"
            t1.insert(END, txt2)

def clear():
    t1.delete("1.0",END)
    t2.delete("1.0", END)
    e1.delete(0,'end')

window=Tk()
window.wm_title('Find My Partnr')

b1=Button(window,text="Search", command=all)
b1.grid(row=0,column=0)
window.bind('<Return>',all)

b2=Button(window,text="clear",command=clear)
b2.grid(row=1,column=0)

e1_value=StringVar()
e1 = Entry(window,width=40,textvariable=e1_value)
e1.grid(row=0,column=3)

sp1 = Spinbox(window, width=30)
sp1.grid(row=3,column=0)

l3=Label(window,width=50,anchor=E,text='Paste here:')
l3.grid(row=0,column=2)

t1_value=StringVar()
t1=Text(window,width = 30)
t1.grid(row=2,column=3)

l1=Label(window,text='Input:')
l1.grid(row=1,column=2)

l2=Label(window,text='Output:')
l2.grid(row=1,column=3)

t2=Text(window,width = 50)
t2.grid(row=2,column=2)

window.mainloop()