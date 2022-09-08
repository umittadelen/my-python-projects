import qrcode
from pyzbar import pyzbar
from PIL import Image

def main():
    cevap = input("ne yapmak istiyorsun (read ; create ; createwifi ; createphone) > ")

    if cevap == "read":
        read()
    
    elif cevap == "create":
        create()
    
    elif cevap == "createwifi":
        createwifi()
    
    elif cevap == "createphone":
        createphone()

    else:
        print("geçerli bir parametre girin")
        main()

def read():
    image = Image.open('C:\\Users\\ÜMİT-İDİL\\Desktop\\python\\qrcode.png')
    qr_code = pyzbar.decode(image)[0]
    data= qr_code.data.decode("utf-8")
    print("sonuç:")
    print(data)
    main()
    
def createwifi():
    name = ""
    pwd = ""
    wpa = ""
    name = input("wifi adını girin > ")
    pwd = input("wifi şifresini girin > ")
    wpa = input("wifi güvenlik protokolü türünü girin (wpa ; wep ; nopass)> ")
    hide = input("wifi gizli mi (true , false) > ")

    input_data = "WIFI:T:{};S:{};P:{};H:{};".format(wpa,name,pwd,hide)

    qr = qrcode.QRCode(
        version=1,
        box_size=input("kutu boyutu > "),
        border=input("dış kenar boyutu > "))
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('C:\\Users\\ÜMİT-İDİL\\Desktop\\python\\qrcode.png')
    main()
    
def create():
    input_data = input("birşey girin > ")
    qr = qrcode.QRCode(
        version=1,
        box_size=input("kutu boyutu > "),
        border=input("dış kenar boyutu > "))
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('C:\\Users\\ÜMİT-İDİL\\Desktop\\python\\qrcode.png')
    main()
    
def createphone():
    number = ""
    msg = ""
    number = input("telefon numarasını girin > ")
    msg = input("okutunca gönderilecek mesajı girin > ")

    input_data = "SMSTO:{}:{}".format(number,msg)

    qr = qrcode.QRCode(
        version=1,
        box_size=input("kutu boyutu > "),
        border=input("dış kenar boyutu > "))
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('C:\\Users\\ÜMİT-İDİL\\Desktop\\python\\qrcode.png')
    main()
main()