import discord
from discord.ext import commands
import linecache
import datetime
import random

TOKEN = ""

bot = commands.Bot(command_prefix=('!'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("On air!")

@bot.command()
async def aes(ctx, *, arg):
    with open('NAMES.txt', 'rt') as file:   
        for index, line in enumerate(file):
            if arg.lower() in line.lower():
                #print(index)
                #await ctx.send(line)
                SAS = linecache.getline('KEYS.txt', index+1)
                SOS = linecache.getline('FULL.txt', index+1)
                #embedVar = discord.Embed(title="Search result", description=arg, color=0x00ff00)
                embedVar = discord.Embed(color=0x6699CC)
                embedVar.add_field(name="Game:", value=SOS, inline=False)
                embedVar.add_field(name="AES key:", value="`"+SAS+"`", inline=False)
                await ctx.send(embed=embedVar)

@bot.command()
async def link(ctx):    
    embedVar = discord.Embed(color=0x666699)
    embedVar.description = "Wow! Is that an **[invite link](https://discord.com/oauth2/authorize?client_id=924010993984622632&scope=applications.commands%20bot&permissions=8)**???"
    await ctx.send(embed=embedVar)

@bot.command()
async def h(ctx):
    embedVar = discord.Embed(title="Help?", color=0x996699)
    embedVar.add_field(name="!aes", value="Search AES key in database by game name. \n`!aes little nightmares 2`", inline=False)
    embedVar.add_field(name="!status ", value="Database status", inline=False)
    embedVar.add_field(name="!link", value="Bot invite link", inline=False)
    embedVar.add_field(name="!data", value="Sends AES database in XLS", inline=False)
    embedVar.add_field(name="!r", value="Message to the creator. \nPlease, technical reports only. \n (new AES keys, AES not working etc)", inline=False)
    embedVar.add_field(name="!git", value="Get bot sources (github link)", inline=False)
    await ctx.send(embed=embedVar)

@bot.command()
async def restart(ctx):
    await ctx.send("nah")


@bot.command()
async def status(ctx):
    lines = 0
    for line in open('KEYS.txt'):
        lines += 1
    embedVar = discord.Embed(title="Total database size", color=0x99CC99)
    embedVar.add_field(name="Games: ", value=lines, inline=True)
    embedVar.add_field(name="Keys: ", value=lines, inline=True)
    embedVar.set_footer(text='Version [Beta 2.4]')
    await ctx.send(embed=embedVar)
#393833273488441345

@bot.command()
async def git(ctx):
    embedVar = discord.Embed(title="Sources", color=0x999999)
    #embedVar.set_thumbnail(url="https://github.githubassets.com/images/modules/logos_page/Octocat.png")
    embedVar.description = "**[GIT](https://github.com/MarkTauber/DMT_bot)**"
    embedVar.set_footer(text='FPSkiller#6474') #, icon_url="https://cdn.discordapp.com/avatars/393833273488441345/589019624907902b5e6e27d6955df53a.png"
    await ctx.send(embed=embedVar)

@bot.command()
async def r(ctx, *, arg):
    load1=discord.Embed(title='collecting data...    [  ' + str(random.randint(1, 25)) + '%   ]',color=0x009999)
    load2=discord.Embed(title='Converting...         [  ' + str(random.randint(25, 50)) + '%  ]',color=0x009999)
    load3=discord.Embed(title='Creating report...    [  ' + str(random.randint(50, 75)) + '%  ]',color=0x009999)
    load4=discord.Embed(title='Sending to server...  [  ' + str(random.randint(75, 100)) + '%  ]',color=0x009999)
    complete=discord.Embed(title='Reported to creator!',color=0x0099CC)
    msg=await ctx.send(embed=load1)
    namos = ctx.author.name
    datetimeString = str(datetime.datetime.now())
    await msg.edit(embed=load2)
    fullreport = "!!!REPORT!!!\nData: [" + datetimeString + "]\nName: [" + namos + "]"
    await msg.edit(embed=load3)
    textxs = "```" + arg + "```"
    await msg.edit(embed=load4)
    print(fullreport)
    print('"' + arg + '"')
    user = await bot.fetch_user(user_id=393833273488441345)
    complete.add_field(name="User", value=namos, inline=True)
    complete.add_field(name="Time", value=datetimeString, inline=True)
    complete.add_field(name="Message: ", value=textxs, inline=False)
    await user.send('__**!!!NEW REORT!!!**__\n > **User:**   `' + namos + "`\n> **Time:**   `"+datetimeString +"`\nMessage:\n" + textxs)
    await msg.edit(embed=complete)
    
bot.run(TOKEN)
