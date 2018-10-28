import discord
import json
import random
import datetime
import requests
import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix="=")

from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
load_opus_lib()

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
        
 

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    in_voice.append(ctx.message.server.id)
    await client.say("<:check:506143689295396874> I have joined your voice channel!")
    
@client.command(pass_context=True)
async def leave(ctx):
    server=ctx.message.server
    voice_client=client.voice_client_in(server)
    await voice_client.disconnect()
    await client.say("<:check:506143689295396874> I have left your voice channel!")
    

@client.command(pass_context=True)
async def play(ctx, *, url):
    opts = {
        'default_search': 'auto',
        'quiet': True,
    }  # youtube_dl options


    
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice.create_ytdl_player(url, ytdl_options=opts)
    players[server.id] = player
    player.start()
        
    

client.run(os.environ['TOKEN'])
