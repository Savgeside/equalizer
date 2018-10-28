import discord
import json
import asyncio
from discord.ext import commands

class Moderation:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def kick(self,ctx,user: discord.Member = None, *, reason = None):
        author = ctx.message.author
        server = ctx.message.server
        try:
            if ctx.message.author.server_permissions.kick_members:
                if user is None:
                    embed = discord.Embed(color=0x36393E)
                    embed.add_field(name="<:error:506132126610227200> Error", value="**Please specify a user for me to kick!**")
                    await self.client.say(embed=embed)
                    return
                await self.client.send_message(user, f"You were kicked from **{server.name}** for the reason of: **{reason}**")
                await self.client.kick(user)
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:check:506143689295396874> Kicked", value=f"<:certified:505938276822024192>User - **{user}** \n :scroll:Reason - **{reason}** \n <:Staff:506124288944766976>Moderator - **{author}**")
                await self.client.say(embed=embed)
            else:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Kick Members**")
                await self.client.say(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**I am missing permissions!**")
            await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def ban(self,ctx,user: discord.Member = None, *, reason = None):
        author = ctx.message.author
        server = ctx.message.server
        try:
            if ctx.message.author.server_permissions.ban_members:
                if user is None:
                    embed = discord.Embed(color=0x36393E)
                    embed.add_field(name="<:error:506132126610227200> Error", value="**Please specify a user for me to ban!**")
                    await self.client.say(embed=embed)
                    return
                await self.client.send_message(user, f"You were banned from **{server.name}** for the reason of: **{reason}**")
                await self.client.ban(user)
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:check:506143689295396874> Banned", value=f"<:certified:505938276822024192>User - **{user}** \n :scroll:Reason - **{reason}** \n <:Staff:506124288944766976>Moderator - **{author}**")
                await self.client.say(embed=embed)
            else:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Ban Members**")
                await self.client.say(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**I am missing permissions!**")
            await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def mute(self,ctx,user: discord.Member = None, *, reason = None):
        with open("Data.json", "r") as f:
            mute = json.load(f)
        server = ctx.message.server
        author = ctx.message.author
        if ctx.message.author.server_permissions.mute_members:
            role = mute[ctx.message.server.id]["mute-role"]
            MutedRole = discord.utils.get(ctx.message.server.roles, name = role)
            if role is None:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="**There is no Muted Role set for this server! You can do: ``=setmute <MutedRole>`` to set it up!**")
                await self.client.say(embed=embed)
                return
            if user is None:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="**Please specify a user for me to mute!**")
                await self.client.say(embed=embed)
                return
            await self.client.add_roles(user, MutedRole)
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:check:506143689295396874> Muted", value=f"<:certified:505938276822024192>User - **{user}** \n :scroll:Reason - **{reason}** \n <:Staff:506124288944766976>Moderator - **{author}**")
            await self.client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Mute Members**")
            await self.client.say(embed=embed)
        with open("Data.json", "w") as f:
            json.dump(mute,f)

    @commands.command(pass_context=True)
    async def unmute(self,ctx,user: discord.Member = None):
        with open("Data.json", "r") as f:
            mute = json.load(f)
        server = ctx.message.server
        author = ctx.message.author
        if ctx.message.author.server_permissions.mute_members:
            role = mute[ctx.message.server.id]["mute-role"]
            MutedRole = discord.utils.get(ctx.message.server.roles, name = role)
            if user is None:
                embed = discord.Embed(color=0x36393E)
                embed.add_field(name="<:error:506132126610227200> Error", value="**Please specify a user for me to unmute!**")
                await self.client.say(embed=embed)
                return
            await self.client.remove_roles(user, MutedRole)
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:check:506143689295396874> Unmuted", value=f"<:certified:505938276822024192>User - **{user}** \n <:Staff:506124288944766976>Moderator - **{author}**")
            await self.client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Mute Members**")
            await self.client.say(embed=embed)
        with open("Data.json", "w") as f:
            json.dump(mute,f)

    @commands.command(pass_context=True)
    async def clear(self, ctx, amount=0):
        if ctx.message.author.server_permissions.manage_messages:
            channel = ctx.message.channel
            messages = []
            async for message in self.client.logs_from(channel, limit=int(amount) + 1):
                messages.append(message)
            await self.client.delete_messages(messages)
            msg = await self.client.say(f'{amount} Message(s) cleared')
            await asyncio.sleep(2)
            await self.client.delete_message(msg)
            return
        else:
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name="<:error:506132126610227200> Error", value="**You are missing permissions!** \n \n :tools:Permissions - **Manage Messages**")
            await self.client.say(embed=embed)

        
            
            

def setup(client):
    client.add_cog(Moderation(client))
