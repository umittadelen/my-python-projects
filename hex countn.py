from colorama import Fore, Style
from PIL import Image

r = 0
g = 0
b = 0
color_list =[]
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def colored(r, g, b, text):
    return "\x1B[38;2;{};{};{}m{}\x1B[0m".format(r, g, b, text)

#                16777216
for f in range(0,16777216):
    hex_color = "#"+hex(f).replace("0x","").zfill(6).upper()
    color_list.append(hex_color)
    print(f)
print(color_list)
MyImg = Image.new( 'RGB', (4096,4096), "white")
pixels = MyImg.load()
for n in range(0, len(color_list)):
    for t in range(MyImg.size[0]):
        for i in range(MyImg.size[1]):
            r,g,b = hex_to_rgb(color_list[n])
            pixels[t,i] = (r, g, b)
            print(colored(r, g, b, hex_color ))
    
MyImg.save("E:\python projeleri\images\imgtest.png")
