from PIL import Image
num_list = ["0","1","2","3","4","5","6","7","8","9"]

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
#16777216
def num_to_hex(num):
    hex_color = "#"+hex(num).replace("0x","").zfill(6).upper()
    return(hex_color)

MyImg = Image.new( 'RGB', (512,512), "white")
pixels = MyImg.load()
'''for i in range(MyImg.size[1]):
    pixels[0,i] = (i, 0, 0)'''
for i in range(0,16):
    r,g,b = hex_to_rgb(num_to_hex(i))
    pixels[0,i] = (r,g,b)
MyImg.save("C:/UsersÜMİT-İDİL/Desktop/img.png")
MyImg.show("C:/UsersÜMİT-İDİL/Desktop/img.png")