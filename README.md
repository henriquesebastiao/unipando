# Unipando Bot

[![CI](https://github.com/henriquesebastiao/unipando/actions/workflows/ci.yml/badge.svg)](https://github.com/henriquesebastiao/unipando/actions/workflows/ci.yml)

Unipando é um bot para o Discord para auxiliar estudantes do curso de Ciência da Computação da UNIP.

## Como Usar

Para adicionar o Unipando ao seu servidor no Discord, siga estas etapas:

1. Acesse o [link de convite](https://discord.com/oauth2/authorize?client_id=1237488134044913827&scope=bot&permissions=621217630912065).
2. Autorize o bot a interagir com seu servidor.

## Comandos

- `?hello` - Hello World!
- `?moeda` - Joga uma moeda para cima.
- `?md <nota-prova> <nota-ava>` - Calcula a média da disciplina `((9 * prova) * ava) / 10`.
- `?mf <nota-md> <nota-exame>` - Calcula a média final da disciplina `(md + exame) / 2`.

## Contribuindo

Variáveis de ambiente:

```dotenv
TOKEN="token-discord"
BOT_ID="bot-id"
```