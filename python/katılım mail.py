import smtplib

gonderen = input("mailinizi girin ")
print(gonderen)
sifresi = input("şifrenizi girin ")
print("kursu istiyorsan 1 istemiyorsan 0 yaz")

m1 = input("PYTHON ")
m2 = input("C++ ")
m3 = input("HTML ")
m4 = input("CSS ")
m5 = input("JAVASCRİPT ")
m6 = input("JAVA ")
isim = input("adını ve soyadını gir ")

alici = "umittaldelen1277@gmail.com"

if(m1 == 1):
    m1 = "PYTHON"
if(m1 == 0):
    m1 = " "
if(m2 == 1):
    m2 = "C++"
if(m2 == 0):
    m2 = " "
if(m3 == 1):
    m3 = "HTML"
if(m3 == 0):
    m3 = " "
if(m4 == 1):
    m4 = "CSS"
if(m4 == 0):
    m4 = " "
if(m5 == 1):
    m5 = "JAVASCRİPT"
if(m5 == 0):
    m5 = " "
if(m6 == 1):
    m6 = "JAVA"
if(m6 == 0):
    m6 = " "


mesaj = "{}, {}, {}, {}, {}, {}, {}, mail= {}".format(m1,m2,m3,m4,m5,m6,isim,gonderen)
 
server = smtplib.SMTP("smtp.gmail.com", '587')
server.starttls()
server.login(gonderen,sifresi)
server.sendmail(gonderen,alici,mesaj)
server.quit()