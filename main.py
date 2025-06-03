import discord  # type: ignore
from discord.ext import commands  # type: ignore
import os
import random

token = os.getenv('DISCORD_TOKEN')



# Intents para acceder a miembros y contenido de mensajes
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Inicialización del bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Diccionario para almacenar partidas por servidor
games = {}

# Comando principal !mafia
@bot.command()
async def crear(ctx, total_players: int):
    guild_id = ctx.guild.id 

    games[guild_id] = {
        "host": ctx.author,
        "total": total_players,
        "players": [],
    }

    await ctx.send(
        f"🎲 Se ha creado una partida de Mafia para {total_players} jugadores. "
        f"Usa `!mafia unirme` para participar."
    )

@bot.command()
async def unirme(ctx):
    guild_id = ctx.guild.id 

    # Unirse a una partida existente
   
    if guild_id not in games:
        await ctx.send(
            "No hay ninguna partida activa. Usa `!mafia crear <número>` para iniciar una."
        )
        return

    game = games[guild_id]



    game["players"].append(ctx.author)

    await ctx.send("tu rol es ciudadano")

if token:
    bot.run(token)
else:
    print("❌ No se encontró el token en las variables de entorno.")