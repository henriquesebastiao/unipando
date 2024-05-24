import asyncio
import os
from datetime import datetime
from secrets import randbelow
from typing import Optional

import discord
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
from dotenv import load_dotenv
from guild import create_class_events, stick_notes
from help import Help
from settings import BOT_ID, COLOR_YELLOW, DEBUG, MODE, PREFIX, TOKEN
from system import System
from unip import Unip

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    activity=discord.Game(name='AVA'),  # Define o que o bot está "jogando"
    aplication_id=os.getenv(BOT_ID),
)

bot.help_command = Help()
scheduler = AsyncIOScheduler()


@bot.event
async def on_ready():
    print(
        f'Logged in as {bot.user} (ID: {bot.user.id}) --> {MODE} (Prefix: {PREFIX})'
    )
    print(
        f'{datetime.now(pytz.timezone("America/Sao_Paulo"))} (America/Sao_Paulo)'
    )
    time_now = f'{datetime.now().isoformat()} (NOW)'
    print(time_now)
    print('-' * len(time_now))

    # Verifica as pendências no servidor Ciência do Desespero
    scheduler.add_job(
        name='Cria eventos de estudo no servidor Ciência do Desespero (alunos de Ciência da Computação).',
        func=create_class_events,
        args=[bot],
        trigger=CronTrigger(hour=15, minute=10, timezone='America/Sao_Paulo'),
    )
    scheduler.add_job(
        name='Envia lembretes de datas importantes no servidor Ciência do Desespero (alunos de Ciência da Computação).',
        func=stick_notes,
        args=[bot],
        trigger=CronTrigger(hour=8, minute=30, timezone='America/Sao_Paulo'),
    )

    scheduler.start()


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        embed = discord.Embed(
            title='Bem vindo ao servidor!',
            description=f'Seja bem vindo {member.mention}, espero que você se divirta!',
            color=COLOR_YELLOW,
        )
        await guild.system_channel.send(embed=embed)


@bot.command(aliases=['ola'])
async def hello(ctx, name: Optional[str]):
    """Diz olá para o usuário."""
    if name is not None:
        await ctx.send(f'Olá, {name}!')
    else:
        await ctx.send('Hello World!')


@bot.command(name='coin', aliases=['moeda'])
async def coin(message):
    """Joga uma moeda para o alto e retorna cara ou coroa."""
    choince = randbelow(2)
    if choince == 0:
        await message.channel.send('Cara 😄')
    else:
        await message.channel.send('Coroa 👑')


# This is a debug command, used to test the bot.
if DEBUG:

    @bot.command(name='debug', aliases=['d'])
    async def debug(ctx):
        """Comando de debug."""
        pass


async def main():
    async with bot:
        await bot.add_cog(Unip(bot))
        await bot.add_cog(System(bot))
        await bot.start(TOKEN)


asyncio.run(main())
