import discord
from discord.ext import commands
import random

discord_intents = discord.Intents.all()
discord_intents.members = True
bot = commands.Bot(command_prefix= a, intents=discord_intents) # a = Префикс
client = commands.Bot(command_prefix= a, intents=discord_intents) # a = Префикс
client.remove_command('help')

@bot.event
async def on_ready():
    print("Бот успешно подключен")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(a + "info")) # a = Префикс
    await bot.wait_until_ready()

@bot.command()
async def info(ctx):
    await ctx.send('Команды')
    await ctx.send(f"{a}rand - случайное число от 0 до 100") # a = Префикс
    await ctx.send(f"{a}role - получение роли") # a = Префикс

@bot.command()
async def rand(ctx):
    await ctx.reply(random.randint(0,100))

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id = a) # a = ID роли, которую нужно выдать новичку
    await member.add_roles(role)

@bot.command()
async def test(ctx):
    await ctx.send('Процесс выдачи роли')
    member = ctx.message.author
    role_1 = member.guild.get_role(a) # a = ID роли, которую нужно выдать
    await member.add_roles(role_1)
    await ctx.send('Роль выдана')

bot.run(config.token)
