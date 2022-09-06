from random import choice,choice,choices
sayilar = (1,2,3,4,5,6,7,8,9,0,"a","b","c","ç","d","e","f","g","ğ",
"h","ı","i","j","k","l","m","n","o","ö","p","q","r","s","ş","t","u",
"ü","v","w","y","z","x","A","B","C","Ç","D","E","F","G","Ğ","H","I",
"İ","J","K","L","M","N","O","Ö","P","Q","R","S","Ş","T","U","Ü","V",
"W","Y","Z","X",".",",",":",";","~","!","'",'"',"^","#","+","$","%",
"&","/","{","(","[",")","]","}","=","?","*","-","_","|","<",">","@")
sifre = str(input("kırılacak şifreyi girin > "))
sifres =""
adim = 0
uzn = 0
while True:
    print("şifreniz deneniyor...",sifres,"  ",adim,"       girilen şifre > ",sifre)
    if sifre == sifres:
        break
    else:
        sifres = ""
        uzn = len(sifre)
        for i in range(uzn):
            sifres += str(choice(sayilar))
            adim += 1
            
print(sifre, "sifreniz ", adim,"denemede bulundu")
input()