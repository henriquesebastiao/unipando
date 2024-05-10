from datetime import date, datetime, timedelta

import discord
from discord.ext import commands


async def create_class_events(bot: commands.Bot):
    """Cria eventos de estudo para a guilda Ciência do Desespero."""
    guild = bot.get_guild(945423070829617262)  # Ciência do Desespero
    channel_event = guild.get_channel(949464732388167680)  # Estudos
    channel_message = guild.get_channel(949092657269993513)  # bot

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
                        event['date'].year,
                        event['date'].month,
                        event['date'].day,
                        20,
                        0,
                    ).astimezone(),
                    description=event['description'],
                    channel=channel_event,
                    privacy_level=discord.PrivacyLevel.guild_only,
                )
                await channel_message.send(
                    f'Evento {event["materia"]} criado para {event["date"].strftime("%d/%m/%y")} as 20:00'
                )
