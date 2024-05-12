from datetime import date, datetime, timedelta

import discord
import pytz
from discord.ext import commands
from dotenv import load_dotenv
from settings import (
    CHANNEL_EVENT_ID,
    CHANNEL_MESSAGE_ID,
    CHANNEL_STICK_NOTES_ID,
    GUILD_ID,
)

load_dotenv()


async def create_class_events(bot: commands.Bot):
    """Cria eventos de estudo para a guilda Ciência do Desespero."""
    guild = bot.get_guild(GUILD_ID)
    channel_event = guild.get_channel(CHANNEL_EVENT_ID)
    channel_message = guild.get_channel(CHANNEL_MESSAGE_ID)

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


async def stick_notes(bot: commands.Bot):
    guild = bot.get_guild(GUILD_ID)
    channel_message = guild.get_channel(CHANNEL_STICK_NOTES_ID)

    dates = [
        {
            'message': 'Hoje é a data limite para postagem das atividades complementares.',
            'date': date(2024, 5, 13),
        },
        {
            'message': 'Hoje se inicia a semana de provas e vai até dia 8. Boa sorte 😄.',
            'date': date(2024, 6, 3),
        },
        {
            'message': 'Hoje é o último dia para a realização das provas!',
            'date': date(2024, 6, 8),
        },
        {
            'message': 'Hoje se inicia a semana de provas substitutivas e vai até dia 15. Boa sorte 🙂.',
            'date': date(2024, 6, 10),
        },
        {
            'message': 'Hoje é o último dia para a realização das provas substitutivas!',
            'date': date(2024, 6, 15),
        },
        {
            'message': 'Hoje se inicia a semana de provas de exame e vai até dia 22. '
            'Boa sorte a todos, vocês vão precisar 😅',
            'date': date(2024, 6, 17),
        },
        {
            'message': 'Hoje é o último dia para a realização das provas de exame!',
            'date': date(2024, 6, 22),
        },
        {
            'message': 'Boas férias (curtas) a todos! 😄',
            'date': date(2024, 6, 24),
        },
    ]

    for date_stick_note in dates:
        if date_stick_note['date'] == datetime.now().date():
            await channel_message.send(date_stick_note['message'])
