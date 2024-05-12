import discord
from discord import ButtonStyle
from discord.ext import commands
from discord.ui import Button, View
from settings import COLOR_YELLOW


class Help(discord.ext.commands.HelpCommand):
    def __init__(self):
        super().__init__()

        # cooldown: Isto fará um cooldown com uma taxa de 2, por 5 com um tipo de balde BucketType.user,
        # que em termos simples, para cada usuário, eles podem chamar o comando duas vezes, a cada 5 segundos.
        self.command_attrs = {
            'name': 'help',
            'aliases': [
                'ajuda',
            ],
            'cooldown': commands.CooldownMapping.from_cooldown(
                2, 5.0, commands.BucketType.user
            ),
            'help': 'Mostra a lista de comandos disponíveis.',
        }

    async def send_bot_help(self, mapping):
        """Envia a mensagem de ajuda para o usuário."""
        embed = discord.Embed(title='Comandos disponíveis', color=COLOR_YELLOW)
        for cog, commandss in mapping.items():
            filtered = await self.filter_commands(commandss, sort=True)
            command_signatures = [
                self.get_command_signature(c) for c in filtered
            ]
            command_descriptions = [c.short_doc for c in filtered]

            values = [
                f'`{signature}` - {description}'
                for signature, description in zip(
                    command_signatures, command_descriptions
                )
            ]

            if values:
                cog_name = getattr(cog, 'qualified_name', 'Sem categoria')
                embed.add_field(
                    name=cog_name,
                    value='\n'.join(values),
                    inline=False,
                )

        view = View()
        view.add_item(
            Button(
                label='Repositório',
                emoji='🗃️',
                style=ButtonStyle.link,
                url='https://github.com/henriquesebastiao/unipando',
            )
        )
        view.add_item(
            Button(
                label='Reporte bugs',
                emoji='💥',
                style=ButtonStyle.link,
                url='https://github.com/henriquesebastiao/unipando/issues',
            )
        )

        channel = self.get_destination()
        await channel.send(embed=embed, view=view)

    async def send_command_help(self, command):
        """Envia a mensagem de ajuda para um comando específico."""
        embed = discord.Embed(
            title=self.get_command_signature(command), color=COLOR_YELLOW
        )
        embed.add_field(
            name='Help', value=command.help
        )  # A descrição do comando é oriuanda das docstrings do comando
        alias = command.aliases
        if alias:
            embed.add_field(
                name='Aliases', value=', '.join(alias), inline=False
            )

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_error_message(self, error):
        """Envia uma mensagem de erro."""
        embed = discord.Embed(
            title='Erro 🤔', description=error, color=COLOR_YELLOW
        )
        channel = self.get_destination()
        await channel.send(embed=embed)
