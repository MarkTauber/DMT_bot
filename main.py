import discord
from discord.ext import commands
import linecache
import datetime
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
                #await ctx.send(SOS)
                #await ctx.send('`' + SAS + '`')
                
@bot.command()
async def link(ctx):    
    embedVar = discord.Embed(color=0x666699)
    embedVar.description = "Wow! Is that an **[invite link](https://discord.com/oauth2/authorize?client_id=924010993984622632&scope=applications.commands%20bot&permissions=8)**???"
    #embedVar.add_field(name="Game:", value="https://discord.com/oauth2/authorize?client_id=924010993984622632&scope=applications.commands%20bot&permissions=8", inline=False)
    await ctx.send(embed=embedVar)
    #await ctx.send("")

@bot.command()
async def h(ctx):
    embedVar = discord.Embed(title="Help?", color=0x996699)
    embedVar.add_field(name="!aes", value="Search AES key in database by game name. \n`!aes little nightmares 2`", inline=False)
    embedVar.add_field(name="!status ", value="Database status", inline=False)
    embedVar.add_field(name="!link", value="Bot invite link", inline=False)
    embedVar.add_field(name="!data", value="Sends AES database in XLS", inline=False)
    embedVar.add_field(name="!r", value="Message to the creator. \nPlease, technical reports only. \n (new AES keys, AES not working etc)", inline=False)
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
    #embedVar.add_field(name=lines, value="", inline=False)
    #embedVar.add_field(name="Keys count:", value=lines, inline=False)
    #embedVar.set_author(name="FPSkiller#6474" , icon_url="https://cdn.discordapp.com/avatars/393833273488441345/589019624907902b5e6e27d6955df53a.png")
    embedVar.add_field(name="Games: ", value=lines, inline=True)
    embedVar.add_field(name="Keys: ", value=lines, inline=True)
    embedVar.set_footer(text='Version [Beta 2.4]')
    #embedVar.set_footer(text='Version [Beta 2.4]', icon_url="https://cdn.discordapp.com/avatars/393833273488441345/589019624907902b5e6e27d6955df53a.png")
    #embedVar.add_field(name="Games count:", value=lines, inline=False)
    #embedVar.add_field(name="Games:", value="`"+SAS+"`", inline=False)
    #embedVar.set_footer(text=ctx.message.author.display_name, icon_url=ctx.message.user.avatarUrl ,inline=False)
    #embedVar.set_footer(text=ctx.message.author.display_name, icon_url=ctx.message.user.avatarUrl ,inline=False)
    #embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/393833273488441345/589019624907902b5e6e27d6955df53a.png") 
    await ctx.send(embed=embedVar)
#393833273488441345

@bot.command()
async def data(ctx):
    await ctx.send(file=discord.File(r'data.xlsx'))

@bot.command()
async def r(ctx, *, arg):
    #guild = ctx.guild
    #name_server = guild.name
    datetimeString = str(datetime.datetime.now())
    #reportes = open("reports.txt", "a")
    #reportes.write("!!!REPORT!!! \n")
    #reportes.write( "[" + name_server + "]\n")
    #reportes.write("Data: [" + datetimeString + "]\n")
    #reportes.write("Name: [" + ctx.author.name + "]\n")
    #reportes.write('LINK: [' + ctx.channel.create_invite(max_uses=1,unique=True) + ']' + "\n")
    #reportes.write('LINK: [' + ctx.channel.icon_url_as(format=None, static_format='webp', size=1024) + ']' + "\n")
    #reportes.write('"' + arg + '"' + "\n\n\n")
    #reportes.close()
    print("!!!REPORT!!!\nData: [" + datetimeString + "]\nName: [" + ctx.author.name + "]")
    print('"' + arg + '"')
    #print("New report by " + ctx.author.name)
    await ctx.send("Reported to creator!")
    

bot.run(TOKEN)


        
