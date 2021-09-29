import discord 
from discord.ext import commands

import json
import os
import random


with open('setting.json','r',encoding='utf8') as jfile:
    jdata= json.load(jfile)
    
bot= commands.Bot(command_prefix= '[')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(F'Loaded.{extension} done')

@bot.command()
async def reload(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(F'Reloaded.{extension}done')

@bot.command()
async def unload(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(F'Unloaded.{extension} done')

for fileName in os.listdir('./cmds'):
    if fileName.endswith('.py'):
        bot.load_extension(f'cmds.{fileName[:-3]}')


@bot.event
async def on_ready():
    print(">> Bot is online<<")

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])