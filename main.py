import discord  # type: ignore
from discord.ext import commands  # type: ignore
import os
import random
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

print(f"Token cargado: {token[:10]}...")

# Intents para acceder a miembros y contenido de mensajes
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Inicialización del bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Diccionario para almacenar partidas por servidor
games = {}

# Comando principal !mafia
@bot.command(name="mafia")
async def mafia(ctx, action: str, *args):
    guild_id = ctx.guild.id

    # Crear una nueva partida
    if action == "crear":
        if guild_id in games:
            await ctx.send("Ya hay una partida en curso.")
            return

        if len(args) != 1 or not args[0].isdigit():
            await ctx.send("Uso: `!mafia crear <número de jugadores>`")
            return

        total_players = int(args[0])
        games[guild_id] = {
            "host": ctx.author,
            "total": total_players,
            "players": [ctx.author],
        }

        await ctx.send(
            f"🎲 Se ha creado una partida de Mafia para {total_players} jugadores. "
            f"Usa `!mafia unirme` para participar."
        )

    # Unirse a una partida existente
    elif action == "unirme":
        if guild_id not in games:
            await ctx.send(
                "No hay ninguna partida activa. Usa `!mafia crear <número>` para iniciar una."
            )
            return

        game = games[guild_id]

        if ctx.author in game["players"]:
            await ctx.send("Ya estás en la partida.")
            return

        game["players"].append(ctx.author)
        await ctx.send

if token:
    bot.run(token)
else:
    print("❌ No se encontró el token en las variables de entorno.")