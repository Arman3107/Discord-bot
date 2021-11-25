import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
#Se importan las distintas librerias necesarias para el funcionamiento del bot

class musica(commands.Cog):
    def __init__(self, client):
     self.client = client
#Se crea la clase musica la cual respondera a los distintos comandos dentro de la app


    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Canal Vacio!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
#Creacion del comando para unirse a un canal de voz 

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()
#Comando para desconectarse de un canal de voz

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format' : "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
            url2 = info['formats'][0]['url']
            ctx.voice_client.play(vc.play(discord.FFmpegPCMAudio(executable = r"C:\Users\Comercia\Desktop\ffmpeg-2021-11-15-git-9e8cdb24cd-full_build\bin\ffmpeg.exe ", source = url2)))
        
 #Comando para reproducir la musica desde un url       
     ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
   }    
#Mejora para el formato de la musica de la libreria Youtube_d1  

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Musica Pausada")
#Comando para pausar la musica 

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Sigue la musica")
#Comando para reiniciar la musica luego de una pausa


def setup(client):
    client.add_cog(musica(client))
