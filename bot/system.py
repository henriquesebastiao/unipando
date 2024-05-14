from datetime import datetime

import discord
import psutil
from discord.ext import commands
from settings import COLOR_BLUE


class System(commands.Cog):
    """Comandos relacionados ao sistema do bot."""

    def __init__(self, bot):
        self.bot = bot
        self.not_allowed_message = (
            'Você não tem permissão para usar este comando 🥲.'
        )

    @commands.command(help='Mostra status do bot.', aliases=['s'])
    async def status(self, ctx):
        system = {
            'CPU': f'{psutil.cpu_percent()}%',
            'RAM': f'{psutil.virtual_memory().percent}%',
            'Disco': f'{psutil.disk_usage("/").percent}%',
            'CPU Freq.': f'{psutil.cpu_freq().current:.2f}Mhz',
            'Total RAM': f'{psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f}GB',
            'Network': f'⬇️ {psutil.net_io_counters().bytes_sent / 1024 / 1024:.2f}MB |'
            f' ⬇️ {psutil.net_io_counters().bytes_recv / 1024 / 1024:.2f}MB',
        }
        embed = discord.Embed(title='System', color=COLOR_BLUE)
        for key, value in system.items():
            embed.add_field(name=key, value=value, inline=True)

        await ctx.send(embed=embed)

    @commands.command(help='Mostra a hora atual do sistema.', aliases=['hora'])
    async def clock(self, ctx):
        embed = discord.Embed(
            title='Hora',
            description=f'{datetime.now().isoformat()}',
            color=COLOR_BLUE,
        )
        await ctx.send(embed=embed)
