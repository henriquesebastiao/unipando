import asyncio
import os
from secrets import randbelow
from typing import Optional

import discord
from discord.ext import commands
from dotenv import load_dotenv
from settings import COLOR_YELLOW
from unip import Unip

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix='?',
    intents=intents,
    activity=discord.Game(name='AVA'),  # Define o que o bot está "jogando"
    aplication_id=os.getenv('BOT_ID'),
)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        embed = discord.Embed(
            title='Bem vindo ao servidor!',
            description=f'Seja bem vindo {member.mention}, espero que você se divirta!',
            color=COLOR_YELLOW,
        )
        await guild.system_channel.send(embed)


@bot.command()
async def hello(ctx, name: Optional[str]):
    """Diz olá para o usuário."""
    if name is not None:
        await ctx.send(f'Hello, {name}!')
    else:
        await ctx.send('Hello World!')


@bot.command()
async def moeda(message):
    """Joga uma moeda para o alto e retorna cara ou coroa."""
    choince = randbelow(2)
    if choince == 0:
        await message.channel.send('Cara 😄')
    else:
        await message.channel.send('Coroa 👑')


async def main():
    async with bot:
        await bot.add_cog(Unip(bot))
        await bot.start(os.getenv('TOKEN'))


asyncio.run(main())
