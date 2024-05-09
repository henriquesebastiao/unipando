from typing import Union

from discord.ext import commands


class Unip(commands.Cog):
    """Comandos relacionados a faculdade, como cálculo de médias, aviosos e etc."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Calcula a média de uma disciplina')
    async def md(self, ctx, prova: Union[int, float], ava: Union[int, float]):
        """Calcula a média de uma disciplina."""
        if prova < 0 or ava < 0:
            await ctx.send('As notas não podem ser negativas! 😅')
        elif prova > 10:
            await ctx.send('Como você tirou mais de 10 na prova? 😅')
        elif ava > 10:
            await ctx.send('Como você tirou mais de 10 no AVA? 😅')
        else:
            media = ((9 * prova) + ava) / 10
            message = (
                f'Prova: {prova:.2f}\n'
                f'AVA: {ava:.2f}\n'
                f'Sua média da disciplina é {media:.2f}'
            )
            if media >= 6:
                message += (
                    f'\nParabéns {ctx.author.mention}, você já está APROVADO!'
                )
            else:
                message += '\nVocê precisa fazer o exame 🥲'
                nota_minima_exame = 10 - media
                message += (
                    f'\n{ctx.author.mention} você deve tirar no mínimo {nota_minima_exame:.2f} '
                    f'no exame para ser aprovado!'
                )
            await ctx.send(message)

    @commands.command(
        help='Calcula a média final de uma disciplina',
    )
    async def mf(
        self,
        ctx,
        media_disciplina: Union[int, float],
        exame: Union[int, float],
    ):
        """Calcula a média final de uma disciplina."""
        if media_disciplina < 0 or exame < 0:
            await ctx.send('As notas não podem ser negativas! 😅')
        elif media_disciplina > 10:
            await ctx.send(
                'Como você tirou mais de 10 na média da disciplina? 😅'
            )
        elif exame > 10:
            await ctx.send('Como você tirou mais de 10 no exame? 😅')
        else:
            media_final = (media_disciplina + exame) / 2
            message = (
                f'Média da disciplina: {media_disciplina:.2f}\n'
                f'Exame: {exame:.2f}\n'
                f'Sua média final é {media_final:.2f}'
            )
            if media_final >= 5:
                message += (
                    f'\nParabéns {ctx.author.mention}, você está APROVADO!'
                )
            else:
                message += (
                    f'\n{ctx.author.mention}, você realmente está REPROVADO 🥲'
                )
            await ctx.send(message)
