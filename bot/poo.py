"""Arquivo que faz o bot ligar.

GitHub: https://github.com/controlado
Repo: https://github.com/controlado/bot-tutorial
Discord: Balaclava#1912
"""

import discord  # py-cord

from utils import dogs

# eventos e comandos são decoradores: ficam em cima de uma função.
# quando esse comando ou evento for acionado, a função abaixo vai
# ser executada automaticamente.

# @bot.event
# eventos são acontecimentos diversos que o bot
# pode identificar e responder aos mesmos.

# @bot.command
# comandos (auto-explicativo) podem ser utilizados
# pelos usuários e o bot pode responder isso.


class MyBot(discord.Bot):  # discord.Bot é a super classe.
    """Essa classe herda todas as características da classe Bot.

    Todas as funções que estão dentro dessa classe, são como parte da classe
    herdeira, por isso, as funções de eventos não precisam ser decoradas com
    @bot.event, basta a função ter o nome do evento, como on_ready.
    """

    permissions = discord.Intents.all()  # criando as permissões do bot.

    def __init__(self) -> None:
        """Essa função é chamada quando instanciar essa classe."""
        super().__init__(intents=self.permissions)

    async def on_ready(self):
        """Essa função é chamada quando o bot ligar."""
        print("o bot foi iniciado com sucesso!")

    async def on_message(self, message: discord.Message):
        """Essa função é chamada quando o bot identificar uma nova mensagem."""
        if message.author.bot:  # se o autor da mensagem for um bot.
            return  # quebra e para o código.

        if "dog" in message.content.lower():  # se "dog" estiver dentro do conteúdo da mensagem.
            dog_image = dogs.get_dog_image()  # puxa uma imagem de cachorro.
            await message.reply(dog_image)  # responde o usuário com a foto.


bot = MyBot()  # instanciando um bot da classe MyBot.


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
