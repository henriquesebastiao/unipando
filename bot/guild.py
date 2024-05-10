import os
from datetime import date, datetime, timedelta

import discord
import pytz
from discord.ext import commands
from dotenv import load_dotenv
from settings import DEBUG

load_dotenv()


async def create_class_events(bot: commands.Bot):
    """Cria eventos de estudo para a guilda Ciência do Desespero."""
    if DEBUG:
        guild = bot.get_guild(int(os.getenv('GUILD_DEV')))
        channel_event = guild.get_channel(int(os.getenv('CHANNEL_EVENT_DEV')))
        channel_message = guild.get_channel(int(os.getenv('CHANNEL_BOT_DEV')))
    else:
        guild = bot.get_guild(int(os.getenv('GUILD')))  # Ciência do Desespero
        channel_event = guild.get_channel(
            int(os.getenv('CHANNEL_EVENT'))
        )  # Estudos
        channel_message = guild.get_channel(
            int(os.getenv('CHANNEL_BOT'))
        )  # bot

    subjects = [
        {
            'materia': 'Sistemas Operacionais Und.3',
            'date': date(2024, 5, 13),
            'description': 'Operação de Sistemas Operacionais.',
        },
        {
            'materia': 'Teoria dos Grafos Und.1',
            'date': date(2024, 5, 20),
            'description': 'Grafos em árvores, Caminho de Euler, caminho de Hamilton e Algoritmo de percurso.',
        },
        {
            'materia': 'Teoria dos Grafos Und.2',
            'date': date(2024, 5, 27),
            'description': 'Árvore mínima, Caminhos mínimos, Problema das quatro cores e Fluxos em Grafos.',
        },
    ]

    existing_events = guild.scheduled_events
    for event in subjects:
        if event['materia'] not in [e.name for e in existing_events]:
            if (
                datetime.now().date()
                <= event['date']
                < datetime.now().date() + timedelta(days=6)
            ):
                await guild.create_scheduled_event(
                    name=event['materia'],
                    start_time=datetime(
                        year=event['date'].year,
                        month=event['date'].month,
                        day=event['date'].day,
                        hour=21,
                        minute=0,
                        second=0,
                        microsecond=0,
                        tzinfo=pytz.timezone('America/Sao_Paulo'),
                    ),
                    description=event['description'],
                    channel=channel_event,
                    privacy_level=discord.PrivacyLevel.guild_only,
                )
                await channel_message.send(
                    f'Evento {event["materia"]} criado para {event["date"].strftime("%d/%m/%y")} '
                    f'as 21h (Horário de Brasília).'
                )
