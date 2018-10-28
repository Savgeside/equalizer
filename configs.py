import discord
import json
from discord.ext import commands

class Configs:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def setwelcome(self,ctx, *, message = None):
        with open("Data.json", "r") as f:
            welcome = json.load(f)
        if ctx.message.author.server_permissions.manage_server:
            if message is None:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="<a:typing:506122373079105557>**Error**: **Didn't state a message** \n :white_check_mark:**Resolution**: **=setwelcome <message>**")
                await self.client.say(embed=embed)
                return
            if not ctx.message.server.id in welcome :
                welcome[ctx.message.server.id] = {}
                welcome[ctx.message.server.id]["welcome"] = "default"
            welcome[ctx.message.server.id]["welcome"] = message
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:check:506143689295396874> Sucess!", value=f"<:submit:505942355581468672>New Message - **{message}**")
            await self.client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Manage Server**")
            await self.client.say(embed=embed)
        with open("Data.json", "w") as f:
            json.dump(welcome,f,indent=4)

    @commands.command(pass_context=True)
    async def setgoodbye(self,ctx, *, message = None):
        with open("Data.json", "r") as f:
            welcome = json.load(f)
        if ctx.message.author.server_permissions.manage_server:
            if message is None:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="<a:typing:506122373079105557>**Error**: **Didn't state a message** \n :white_check_mark:**Resolution**: **=setwgoodbye <message>**")
                await self.client.say(embed=embed)
                return
            if not ctx.message.server.id in welcome :
                welcome[ctx.message.server.id] = {}
                welcome[ctx.message.server.id]["goodbye"] = "default"
            welcome[ctx.message.server.id]["goodbye"] = message
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:check:506143689295396874> Sucess!", value=f"<:submit:505942355581468672>New Message - **{message}**")
            await self.client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Manage Server**")
            await self.client.say(embed=embed)
        with open("Data.json", "w") as f:
            json.dump(welcome,f,indent=4)

    @commands.command(pass_context=True)
    async def setchannel(self,ctx, *, channel = None):
        with open("Data.json", "r") as f:
            welcome = json.load(f)
            channel2 = discord.utils.get(ctx.message.server.channels, name  = channel)
        if ctx.message.author.server_permissions.manage_server:
            if channel2 is None:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="**Please specify a channel in this server!**")
                await self.client.say(embed=embed)
                return
            if not ctx.message.server.id in welcome :
                welcome[ctx.message.server.id] = {}
                welcome[ctx.message.server.id]["channel"] = "default"
            welcome[ctx.message.server.id]["channel"] = channel
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:check:506143689295396874> Sucess!", value=f"<:submit:505942355581468672>New Channel - **{channel}**")
            await self.client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Manage Server**")
            await self.client.say(embed=embed)
        with open("Data.json", "w") as f:
            json.dump(welcome,f,indent=4)

    @commands.command(pass_context=True)
    async def setmute(self,ctx, *, role = None):
        with open("Data.json", "r") as f:
            welcome = json.load(f)
        MuteRole = discord.utils.get(ctx.message.server.roles, name  = role)
        if ctx.message.author.server_permissions.manage_server:
            if MuteRole is None:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="**Please specify a role in this server!**")
                await self.client.say(embed=embed)
                return
            if not ctx.message.server.id in welcome :
                welcome[ctx.message.server.id] = {}
                welcome[ctx.message.server.id]["mute-role"] = "default"
            welcome[ctx.message.server.id]["mute-role"] = role
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:check:506143689295396874> Sucess!", value=f"<:submit:505942355581468672>New Mute Role - **{role}**")
            await self.client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Manage Server**")
            await self.client.say(embed=embed)
        with open("Data.json", "w") as f:
            json.dump(welcome,f,indent=4)

def setup(client):
    client.add_cog(Configs(client))

    
