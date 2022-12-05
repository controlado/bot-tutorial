"""Arquivo que faz o bot ligar.

Paradigma: programação funcional.

GitHub: https://github.com/controlado
Repo: https://github.com/controlado/bot-tutorial
Discord: Balaclava#1912
"""

import discord  # py-cord

from utils import dogs

permissions = discord.Intents.all()  # criando as permissões do bot.
bot = discord.Bot(intents=permissions)  # criando o bot e dando as permissões.

# eventos e comandos são decoradores: ficam em cima de uma função.
# quando esse comando ou evento for acionado, a função abaixo vai
# ser executada automaticamente.

# @bot.event
# eventos são acontecimentos diversos que o bot
# pode identificar e responder aos mesmos.

# @bot.command
# comandos (auto-explicativo) podem ser utilizados
# pelos usuários e o bot pode responder isso.


@bot.event  # registrando a função abaixo como uma resposta ao evento.
# evento on_ready: https://docs.pycord.dev/en/stable/api/events.html#discord.on_ready
async def on_ready():
    """Essa função é chamada quando o bot ligar."""
    print("o bot foi iniciado com sucesso!")  # mostra a mensagem no console.


@bot.event  # registrando a função abaixo como uma resposta ao evento.
# evento on_message: https://docs.pycord.dev/en/stable/api/events.html#discord.on_message
async def on_message(message: discord.Message):
    """Essa função é chamada quando o bot identificar uma nova mensagem."""
    if message.author.bot:  # se o autor da mensagem for um bot.
        return  # quebra e para o código.

    if "dog" in message.content.lower():  # se "dog" estiver dentro do conteúdo da mensagem.
        dog_image = dogs.get_dog_image()  # puxa uma imagem de cachorro.
        await message.reply(dog_image)  # responde o usuário com a foto.


@bot.command(name="cachorro", description="vou enviar uma foto de um cachorro")
# registrando um comando: https://docs.pycord.dev/en/stable/api/application_commands.html#discord.commands.command
# e que a função abaixo vai ser a resposta à esse comando registrado.
async def dog(ctx: discord.commands.ApplicationContext, breed: str = None):
    """Essa função é chamada quando o comando "cachorro" for acionado.

    Vai responder o usuário com link de uma foto de cachorro aleatório caso
    não tenha o parâmetro breed, caso tenha, vai responder com uma foto que
    corresponda à raça.

    O parâmetro ctx é o contexto da situação em que foi utilizado o comando,
    sempre que o comando é utilizado, a função é chamada com este parâmetro.

    Parâmetros:
        ctx (ApplicationContext): Contexto do comando.
        breed (str, optional): Raça do cachorro.
    """
    await ctx.defer()  # faz o bot esperar (bot está pensando...)
    dog_image = dogs.get_dog_image(breed)  # puxa uma imagem de cachorro.
    await ctx.respond(dog_image)  # responde o usuário com a foto.

# usa a função run() que está dentro do bot pra fazê-lo ligar efetivamente.
# a função run() precisa do token do bot pra conseguir fazer as conexões.
bot.run("MTA0OTM4ODM4NDg3MjgyODkyOA.G43H2i.Yp3vmLGPZiLdgNMtng5YLvmUbnfap4t9QP3nVA")
