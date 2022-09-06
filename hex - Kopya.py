from PIL import Image
import random
num_list = ["0","1","2","3","4","5","6","7","8","9"]

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
#16777216
def num_to_hex(num):
    hex_color = "#"+hex(num).replace("0x","").zfill(6).upper()
    return(hex_color)

MyImg = Image.new( 'RGB', (512,512), "white")#4096
pixels = MyImg.load()
'''for i in range(MyImg.size[1]):
    pixels[0,i] = (i, 0, 0)'''
for i in range(0,512):
    r,b,g = hex_to_rgb(num_to_hex(12777000))
    pixels[0,i] = (r,g,b)
    for f in range(0,512):
        r,g,b = hex_to_rgb(num_to_hex(random.randint(0,12777000)))
        pixels[f,i] = (r,g,b)
        for a in range(random.randint(0,2),random.randint(2,4)):
            r,g,b = hex_to_rgb(num_to_hex(r+i*f+a+1000))
            pixels[a,f] = (r,g,b)
            print(i,"\t",f,"\t",a)
print("image generated")
MyImg.save("img.png")
MyImg.show("img.png")