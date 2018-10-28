import discord
import json
import random
import datetime
import requests
import asyncio
from discord.ext import commands

TOKEN = "NTA2MTE2Nzk0NzUxMjU0NTM5.Drddiw.C_gCrA99x9rVj6qfN0ZK1z6eOi8"

client = commands.Bot(command_prefix="=")

@client.event
async def on_ready():
    print("Ready")

extensions = ['moderation', 'configs']
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command(pass_context=True)
async def load(ctx, extension):
    if ctx.message.author.id == "481270883701358602":
        try:
            client.load_extension(extension)
            print(f'Loaded {extension}')
            msg = await client.say(f"<a:Reloading:506169879792189440> loading **{extension}**")
            await asyncio.sleep(5)
            await client.edit_message(msg, f"<:check:506143689295396874> loaded **{extension}**")
        except Exception as error:
                print('{} cannot be loaded. [{}]'.format(extension, error))
                await client.say('<:error:506132126610227200> **​{}** cannot be reloaded. **[{}]**'.format(extension, error))
    else:
        await client.say("**You can't use this. My creator can only use this.**")

@client.command(pass_context=True)
async def unload(ctx, extension):
    if ctx.message.author.id == "481270883701358602":
        try:
            client.unload_extension(extension)
            print(f'Unloaded {extension}')
            msg = await client.say(f"<a:Reloading:506169879792189440> unloading **{extension}**")
            await asyncio.sleep(5)
            await client.edit_message(msg, f"<:check:506143689295396874> unloaded **{extension}**")
        except Exception as error:
                print('{} cannot be unloaded. [{}]'.format(extension, error))
                await client.say('<:error:506132126610227200> **​{}** cannot be reloaded. **[{}]**'.format(extension, error))
    else:
        await client.say("**You can't use this. My creator can only use this.**")

@client.command(pass_context=True)
async def reload(ctx):
    if ctx.message.author.id == "481270883701358602":
        try:
            client.unload_extension(extension)
            client.load_extension(extension)
            msg = await client.say(f"<a:Reloading:506169879792189440> reloading Cogs")
            await asyncio.sleep(5)
            await client.edit_message(msg, f"<:check:506143689295396874> reloaded Cogs")
        except Exception as error:
                print('{} cannot be reloaded. [{}]'.format(extension, error))
                await client.say('<:error:506132126610227200> **​{}** cannot be reloaded. **[{}]**'.format(extension, error))
    else:
        await client.say("**You can't use this. My creator can only use this.**")

    
    


        
    

client.run(TOKEN)
