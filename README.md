# Text Generator and Translator API

Este projeto é uma API de geração de texto e tradução de texto do inglês para o francês construída com FastAPI e utilizando os modelo GPT-2 (geração de texto) e Helsinki-NLP/opus-mt-en-fr (tradução).

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/pedromvba/data-driven-apps-tp2-part1.git
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python3 -m venv .venv
    source venv/bin/activate  # Para Mac/Linux
    .\venv\Scripts\activate   # Para Windows
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute a aplicação:
    ```sh
    uvicorn src.main:app --reload
    ```

2. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Endpoints

### `POST /textgen/`

Gera texto baseado na mensagem fornecida.

#### Exemplo de Requisição

```json
{
    "message": "Olá, como você está?"
}
```

#### Exemplo de Resposta
```json
{
    "bot_message": "Olá, como você está? Eu estou bem, obrigado por perguntar."
}
```

## Dependências

* transformers==4.46.0
* uvicorn==0.32.0
* fastapi==0.115.4
* torch==2.5.1
* sentencepiece==0.2.0


### `POST /en-fr-translator/`

Traduz o texto da mensagem fornecida do inglês para o francês.

#### Exemplo de Requisição

```json
{
    "message": "Good Morning"
}
```

#### Exemplo de Resposta
```json
{
    "bot_message": "Bonjour."
}
```

## Dependências

* transformers==4.46.0
* uvicorn==0.32.0
* fastapi==0.115.4
* torch==2.5.1
* sentencepiece==0.2.0