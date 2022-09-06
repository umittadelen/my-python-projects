import tkinter as tk
from tkinter import *
from random import choice,choice

sayilar = (1,2,3,4,5,6,7,8,9,0,"a","b","c","ç","d","e","f","g","ğ",
"h","ı","i","j","k","l","m","n","o","ö","p","q","r","s","ş","t","u",
"ü","v","w","y","z","x","A","B","C","Ç","D","E","F","G","Ğ","H","I",
"İ","J","K","L","M","N","O","Ö","P","Q","R","S","Ş","T","U","Ü","V",
"W","Y","Z","X",".",",",":",";","~","!","'",'"',"^","#","+","$","%",
"&","/","{","(","[",")","]","}","=","?","*","-","_","|","<",">","@","\\")

sifres =""
uzn = 0

def degistir(val):
    sayi1.delete(1.0,END)
    uzn = val
    sifres =""
    for i in range(int(uzn)):
        sifres += str(choice(sayilar))
    sayi1.insert(INSERT,str(sifres))
    
pencere = tk.Tk()
pencere.geometry("500x120")

slider = tk.Scale(from_=2,to=40,orient=HORIZONTAL,command=degistir)
slider.place(x=10,y=10)

sayi1 = Text(width=40,height=1,font="calibri 14 bold")
sayi1.place(x=10,y=80)

pencere.mainloop()