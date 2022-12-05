# `#️⃣` `Discord Bot Tutorial`

### `☕` [About me](https://github.com/controlado)
- ![info](https://img.shields.io/static/v1?logo=discord&label=&message=Balaclava%231912&color=4078c0&logoColor=white&style=flat)
![info](https://wakatime.com/badge/user/89c5e1c8-9e67-43ef-bd0e-3ff9a4fde5e2/project/612c1050-ee90-437b-ba74-3edac26682a6.svg?style=flat)
- ![language](https://img.shields.io/static/v1?logo=Python&label=&message=Python%203.11&color=4078c0&logoColor=white&style=flat)
![language](https://img.shields.io/static/v1?label=&message=Pycord&color=4078c0&logoColor=white&style=flat)
![language](https://img.shields.io/static/v1?label=&message=Requests&color=4078c0&logoColor=white&style=flat)
- ![ide](https://img.shields.io/static/v1?logo=Visual%20Studio%20Code&label=&message=Visual%20Studio%20Code&color=4078c0&logoColor=white&style=flat)
![ide](https://img.shields.io/static/v1?logo=Github&label=&message=MIT&color=4078c0&logoColor=white&style=flat)

#

### `⚙️` [Comandos](https://docs.pycord.dev/en/stable/api/application_commands.html#commands)

<details>
    <summary> parâmetro opcional (explicação) </summary>
    
  ```python
    @bot.command(name="cachorro", description="vou enviar uma foto de um cachorro")
    # essa linha mostra pra o discord que a função abaixo vai ser a resposta do comando "cachorro".
    async def dog(ctx: discord.commands.ApplicationContext, breed: str = None):
        """Essa função vai ser chamada quando o comando "cachorro" for executado.
        
        O parâmetro ctx contem várias informações sobre o uso do comando, como por exemplo
        quem utilizou, em qual canal foi utilizado, a mensagem que acionou o comando...

        Já o parâmetro breed, quem decide se vai utilizar ou não é o usuário que executar
        o comando, esse é um parâmetro opcional.
        """
        await ctx.defer()  # faz o bot esperar (bot está pensando...)
  ```

</details>

#

### `👀` [Eventos](https://docs.pycord.dev/en/stable/api/events.html#event-reference)

<details>
    <summary> on_ready (explicação) </summary>
    
  ```python
    @bot.event
    # essa linha mostra pra o discord que a função abaixo vai ser a resposta de um evento.
    # qual evento? o nome da função abaixo vai discernir isso.
    async def on_ready():
        """Quando o bot ligar, ele executa essa função.
        
        É assim que funciona: cada evento é acionado de uma maneira diferente.
        
        Quando um evento for acionado, o discord vai procurar no seu código se
        você configurou uma resposta pra esse evento, se sim, ele vai executar
        essa resposta de forma automática.

        Nesse caso, quando o bot ligar, ele vai procurar no seu código se você
        configurou uma resposta pra o evento on_ready.
        """
        print("o bot foi iniciado com sucesso!")
  ```

</details>

<details>
    <summary> on_message </summary>
    
  ```python
    @bot.event
    async def on_message(message: discord.Message):
        """Quando o bot identificar uma nova mensagem, ele executa essa função.
        
        Nesse caso, o evento on_message envia para as funções de resposta, a mensagem
        que foi identificada, por isso, nas suas funções on_message, você deve esperar
        um argumento do tipo discord.Message.
        """
        print("opa! uma mensagem foi identificada.")
  ```

</details>

#

### `⚠️` [License](https://choosealicense.com/licenses/mit/)
