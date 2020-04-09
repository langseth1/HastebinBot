import discord
from discord.ext import commands
from aiohttp import ClientSession
import datetime
from json import load

#Variables
with open("token.json") as file:
    data = load(file)
token = data["token"]

bot = commands.Bot(command_prefix="h!")

#Hastebin
async def post(content, url='https://hastebin.com'):
    async with ClientSession() as session:
        async with session.post(f'{url}/documents', data=content.encode('utf-8')) as post:
            return url + '/' + (await post.json())['key']

#Events
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="h!haste {insert text}"))

@bot.event
async def on_guild_join(guild):
    print("Joined guild: ", guild)

@bot.event
async def on_guild_remove(guild):
    print("Removed from guild: ", guild)
    

#Commands
@bot.command()
async def haste(ctx):
    time = datetime.datetime.now()
    embed = discord.Embed(title="Hastebin link", color=discord.Color.blue(), url=await post(content = ctx.message.content[8:], url='https://hastebin.com'))
    
    embed.set_author(name="HastebinBot", icon_url="https://www.saashub.com/images/app/service_logos/10/2e5b036c770f/large.png?1528818030")
    embed.set_footer(text=f"Requested by: {ctx.author.name} on: {time} ", icon_url=ctx.author.avatar_url)

    message = ctx.message

    await ctx.send(embed=embed)
    await message.delete()
    
    





bot.run(token)