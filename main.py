import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

list = ['ЭКОНОМЬТЕ РЕСУРСЫ',
        'РАЗДЕЛЯЙТЕ МУСОР',
        'СДАВАЙТЕ ВТОРСЫРЬЁ',
        'ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ',
        'ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ',
        'ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ',
        'ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ',
        'ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА']

list_2 = ['сокращение озонового слоя', 
          'глобальное потепление', 
          'загрязнение атмосферы', 
          'парниковый эффект', 
          'загрязнение Мирового океана', 
          'сокращение многообразия биологических видов',]

@bot.command()
async def hello(ctx):
    await ctx.send(f'привет я бот могу рассказать о проблемах и способах их решения.')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def eco(ctx):
    element = random.choice(list)
    await ctx.send(element)

@bot.command()
async def Problems(ctx):
    element = random.choice(list_2)
    await ctx.send(element)

bot.run("")
