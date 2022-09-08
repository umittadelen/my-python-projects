import qrcode
import discord
from discord.ext import commands
from discord.utils import get
from pyzbar import pyzbar
from PIL import Image
import os

username = os.getlogin()
f = open("C:\\Users\\{}\\Desktop\\python\\token.txt".format(username), "r")
token = f.read()
f.close()

client = commands.Bot(command_prefix= 'qr.')

@client.event
async def on_ready():
    print("bot is ready")


@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 998971937835462696:
        if payload.emoji.name == "❌":
            channel = client.get_channel(998971937835462696)
            user = payload.member
            message = await channel.fetch_message(payload.message_id)
            reaction = get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count >= 2:
                await message.delete()
                await message.delete()
                print("mesaj silindi\nmesajı silen: {}".format(user))

@client.command(aliases=["link."])
async def link(ctx , *, link):
    input_data = link
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('C:\\Users\\{}\\Desktop\\python\\qrcode.png'.format(username))
    message = await ctx.send(file=discord.File('C:\\Users\\{}\\Desktop\\python\\qrcode.png'.format(username)))
    await message.add_reaction('❌')
    print("link oluşturuldu:\n{}".format(input_data))
    
@client.command(aliases=["text."])
async def text(ctx , *, text):
    input_data = text
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('C:\\Users\\{}\\Desktop\\python\\qrcode.png'.format(username))
    message = await ctx.send(file=discord.File('C:\\Users\\{}\\Desktop\\python\\qrcode.png'.format(username)))
    await message.add_reaction('❌')
    print("yazı oluşturuldu:\n{}".format(input_data))

@client.command(aliases=["number."])
async def number(ctx , *, number):
    input_data = "SMSTO:{}:".format(number)
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('C:\\Users\\{}\\Desktop\\python\\qrcode.png'.format(username))
    message = await ctx.send(file=discord.File('C:\\Users\\{}\\Desktop\\python\\qrcode.png'.format(username)))
    await message.add_reaction('❌')
    print("telefon numarası oluşturuldu:\n{}".format(input_data))

client.run(token)