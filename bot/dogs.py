"""Responsável por funções que retornam alguma coisa.

GitHub: https://github.com/controlado
Discord: Balaclava#1912
"""

import requests  # módulo responsável por fazer requisições.


def get_dog_image(breed: str = None) -> str:
    """Retorna o link de alguma imagem de cachorro.

    Caso receba uma raça como parâmetro, vai ser retornado
    fotos de cachorros com a raça requisitada, caso válida.

    Parâmetros:
        breed (str, optional): Raça do cachorro.

    Retorna:
        str: Link da foto.
    """
    base_url = "https://dog.ceo/api"  # url da api.

    if breed:
        api_url = f"{base_url}/breed/{breed}/images/random"
    else:
        api_url = f"{base_url}/breeds/image/random"

    response = requests.get(api_url)  # acessa a página.
    response_dict = response.json()  # acessa o json.
    return response_dict["message"]  # busca o valor "message".
