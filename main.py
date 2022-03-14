import discord
from discord.ext import commands

from webserver import keep_alive
import os

bot = commands.Bot("cu!")


@bot.event
async def on_ready():
    print(f'chupa carlos, sou {bot.user}')


@bot.event
async def on_menssage(message):
    if message.author == bot.user:
        return


@bot.command(name="chupe")
async def humilhar(ctx):
    resposta = "robou meu código caralho"
    await ctx.send(resposta)


@bot.command(name="gostosa")
async def gostosa(ctx):
    isso = "o gostoso do erick me criou e sou uma gostosa"
    await ctx.send(isso)


@bot.command(name="comandos")
async def gostosa(ctx):
    isso = " use cu! para me convocar \n chupe (humilha o carlos) \n gostosa (chama eu e o erick de gostosa) \n puta (teu emprego) \n carlos (verdades) \n questionavel (verdades) \n lixo (cs) \n aprender (links de tutorias) \n integrar (link de convite do bot) \n gostoso (voz do gostoso) \n gremio (gremio) \n vasco (o vasco kkkk) \n peitos (deadpool)"
    await ctx.send(isso)


@bot.command(name="puta")
async def gostosa(ctx):
    isso = "seu novo trabalho de puta é interessante"
    await ctx.send(isso)


@bot.command(name="carlos")
async def gostosa(ctx):
    isso = "carlos 2cm"
    await ctx.send(isso)


@bot.command(name="questionavel")
async def gostosa(ctx):
    isso = "esse bot deveria existir ?"
    await ctx.send(isso)

@bot.command(name="gremio")
async def gostosa(ctx):
    await ctx.send('como isso afeta o gremio?', file=discord.File("imagens/gremio.jpeg"))

@bot.command(name="vasco")
async def gostosa(ctx):
    await ctx.send('o vasco existe?', file=discord.File("imagens/vasco.jpg"))

@bot.command(name="peitos")
async def gostosa(ctx):
    await ctx.send('gosotosa', file=discord.File("imagens/peitos.jpg"))

@bot.command(name="gostoso")
async def gostosa(ctx):
    await ctx.send('como isso afeta o gremio?', file=discord.File("imagens/gostoso.ogg"))

@bot.command(name="lixo")
async def gostosa(ctx):
    isso = "aprende a jogar cs teu lixo"
    await ctx.send(isso)


@bot.command(name="aprender")
async def gostosa(ctx):
    isso = "C = https://www.youtube.com/watch?v=87SH2Cn0s9A \n C# = https://www.youtube.com/watch?v=wxznTygnRfQ \n Python = https://www.youtube.com/watch?v=XKHEtdqhLK8 \n Java = https://www.youtube.com/watch?v=xk4_1vDrzzo"
    await ctx.send(isso)

@bot.command(name="integrar")
async def gostosa(ctx):
    isso = "https://discord.com/api/oauth2/authorize?client_id=952616643446591570&permissions=2048&scope=bot"
    await ctx.send(isso)

@bot.command("yo")
async def humilhar(ctx):
    resposta = "eu sou astolfo um bot vagabundo"
    await ctx.send(resposta)

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)