import discord
from discord.ext import commands
import linecache
import datetime
import asyncio
import random
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import codecs
import filecmp

TOKEN = "TOKEN!!!"

bot = commands.Bot(command_prefix=('!'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("On air!")



@bot.command()
async def aes(ctx, *, arg):
    if len(arg.replace(" ", "")) < 3 :
        embedVar = discord.Embed(color=0x669999)
        embedVar.add_field(name="Nope!", value="Request will be executed with 3+ characters only", inline=False)
        await ctx.send(embed=embedVar)
    else:
        with open('AES.txt', 'rt') as file:   
            for index, line in enumerate(file):
                search = re.sub("[:|']","",arg)
                lst = line.split()
                loh = lst[:-1]
                strings = " "
                jopa = strings.join(loh)
                #print (jopa)
                where = re.sub("[:|']","",jopa)
                
                if str(search.lower()) in str(where.lower()):
                    lst = line.split()
                    loh = lst[:-1]
                    stringos = " "
                    embedVar = discord.Embed(color=0x6699CC)
                    embedVar.add_field(name="Game:", value=stringos.join(loh), inline=False)
                    embedVar.add_field(name="AES key:", value="`"+lst[-1]+"`", inline=False)
                    await ctx.send(embed=embedVar)





@bot.command()
async def link(ctx):    
    embedVar = discord.Embed(color=0x666699)
    embedVar.description = "Wow! Is that an **[invite link](https://discord.com/oauth2/authorize?client_id=924010993984622632&scope=applications.commands%20bot&permissions=8)**?"
    await ctx.send(embed=embedVar)

    

@bot.command()
async def data(ctx):   
   await ctx.send(file=discord.File(r'AES.txt'))
    

@bot.command()
async def h(ctx):
    embedVar = discord.Embed(title="Help?", color=0x996699)
    embedVar.add_field(name="!aes", value="Search AES key in database by game name. \n`!aes little nightmares`", inline=False)
    embedVar.add_field(name="!status ", value="Database status", inline=False)
    embedVar.add_field(name="!link", value="Bot invite link", inline=False)
    embedVar.add_field(name="!data", value="Sends AES database", inline=False)
    embedVar.add_field(name="!r", value="Message to the creator. \nPlease, technical reports only. \n (new AES keys, AES not working etc)", inline=False)
    embedVar.add_field(name="!git", value="Get bot sources (github link)", inline=False)
    await ctx.send(embed=embedVar)


@bot.command()
async def status(ctx):
    lines = 0
    sosi = open('AES.txt', "r")
    for line in sosi:
        lines += 1
    embedVar = discord.Embed(title="Total database size", color=0x99CC99)
    embedVar.add_field(name="Keys: ", value=lines, inline=True)
    embedVar.set_footer(text='Version [Beta 4]')
    await ctx.send(embed=embedVar)


@bot.command()
async def git(ctx):
    embedVar = discord.Embed(title="Sources", color=0x999999)
    embedVar.description = "**[GIT](https://github.com/MarkTauber/DMT_bot)**"
    embedVar.set_footer(text='FPSkiller#6474')
    await ctx.send(embed=embedVar)


@bot.command()
async def pa(ctx, chat, IDEW, *, answer):
        if ctx.author.id == 393833273488441345:  #393833273488441345 is my user ID
            user = await bot.fetch_user(user_id=chat)
            await user.send("> Your report **[" + str(IDEW) + "]** has been answered\n\n" + str(answer))  
            await ctx.send("Reply has been sent!")

@bot.command()
async def ca(ctx, channel: discord.TextChannel, REPORTS, *, text):
    if ctx.author.id == 393833273488441345:  #393833273488441345 is my user ID
        emb= discord.Embed(title='Report ' + str(REPORTS) + " answered",description=f'{text}', timestamp=ctx.message.created_at, color=0xCC3300)
        await channel.send(embed=emb)
        await ctx.send("Reply has been sent!")



@bot.command()
async def r(ctx, *, arg):
    load1=discord.Embed(title='collecting data...    `[  ' + str(random.randint(1, 10)) + '%   ]`',color=0x009999)
    load2=discord.Embed(title='Converting...         `[  ' + str(random.randint(10, 36)) + '%  ]`',color=0x009999)
    load3=discord.Embed(title='Creating report...    `[  ' + str(random.randint(36, 83)) + '%  ]`',color=0x009999)
    load4=discord.Embed(title='Sending to server...  `[  ' + str(random.randint(83, 100)) + '%  ]`',color=0x009999)
    complete=discord.Embed(title='Reported to creator!',color=0x0099CC)
    msg=await ctx.send(embed=load1)
    namos = ctx.author.name
    sos = ctx.channel.id
    ses = ctx.message.author.id
    datetimeString = str(datetime.datetime.now())
    await asyncio.sleep(random.uniform(0, 0.5))
    await msg.edit(embed=load2)
    fullreport = "!!!REPORT!!!\nData: [" + datetimeString + "]\nName: [" + namos + "]"
    await asyncio.sleep(random.uniform(0, 0.5))
    await msg.edit(embed=load3)
    textxs = "```" + arg + "```"
    IDs = random.randint(1000000000, 9999999999)
    await asyncio.sleep(random.uniform(0, 0.5))
    await msg.edit(embed=load4)
    print(fullreport)
    print('"' + arg + '"')
    
    user = await bot.fetch_user(user_id=393833273488441345)
    complete.add_field(name="User", value=namos, inline=True)
    complete.add_field(name="Time", value=datetimeString, inline=True)
    complete.add_field(name="Message: ", value=textxs, inline=False)
    complete.set_footer(text="ID_" + str(IDs) + "")
    await user.send('__**!!!NEW REPORT!!!**__\n> **User:**   `' + namos + 
    "`\n> **Time:**  `"+ datetimeString + 
    "`\n\n> CHAT ID:       `" + str(sos) + 
    "`\n> USER ID:        `" + str(ses) + "`" + 
    "\n> REPORT ID:   `" + str(IDs) + "`\n\n" + textxs)
    await msg.edit(embed=complete)
    
    
@bot.command()
async def update(ctx):
    if ctx.author.id == 393833273488441345:  #393833273488441345 is my user ID
        await ctx.send("Update started")
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
        driver.get("https://cs.rin.ru/forum/viewtopic.php?f=10&t=100672")
        await ctx.send("waiting...")
        print("waiting...")
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div[2]/div[2]/table[3]/tbody/tr[3]/td[2]/table/tbody/tr/td/div[1]/div[3]/div[1]/input").click()
        test_string = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div[2]/div[2]/table[3]/tbody/tr[3]/td[2]/table/tbody/tr/td/div[1]/div[3]/div[2]/div/div/div[2]/div/ol").text
        f1 = open("text1.txt", 'w') 
        f1.write(test_string)
        driver.close()
        await ctx.send("Looking for new keys...")
        print("Looking for new keys...")
        lines = 0
        for line in open('text1.txt'):
                lines += 1

        lines2 = 0
        for line in open('AES.txt'):
                lines2 += 1

        if lines > lines2-1:

            #f4 = open("AES.txt", 'w') 
            #f5= open("text1.txt",'r')
            BLOCKSIZE = 1048576 # or some other, desired size in bytes
            with codecs.open('text1.txt', "r", "ANSI") as sourceFile:
                with codecs.open('AES.txt', "w", "utf-8") as targetFile:
                    while True:
                        contents = sourceFile.read(BLOCKSIZE)
                        if not contents:
                              break
                        targetFile.write(contents)

    #f4.write(f5.read())
    #f4.close()
    #f5.close()
            f44 = open("AES.txt", 'a') 
            f44.write("\nFortnite 20.10	0x59BD2F0BB25EDFACD988FE48289D32E31CF22F8F5344C5F7769089ED7355473C")
            f44.close()
            
            f12 = open("text1.txt", 'w') 
            f12.write("")
            f12.close
    
            f13 = open("geckodriver.log", 'w') 
            f13.write("")
            f13.close()
    
            await ctx.send("Successfully updated!")
            print("Successfully updated!")
            
            
            
            
            
        else:
            f12 = open("text1.txt", 'w') 
            f12.write("")
            f12.close
            f13 = open("geckodriver.log", 'w') 
            f13.write("")
            f13.close()
            await ctx.send("Nothing new")
            print("Nothing new")

bot.run(TOKEN)
