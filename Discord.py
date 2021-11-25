import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import Musica

cogs = [Musica]

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run()
