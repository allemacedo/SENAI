# Projeto 8: Sua Primeira API de Streaming de Filmes 🎬
---
## O Cenário 👨‍💼

Você acabou de conseguir um estágio na "PyFlix", a mais nova startup com a ambição de se tornar a maior plataforma de streaming de filmes do mundo. Sua primeira tarefa é construir o pilar de todo o serviço: a API do catálogo de filmes.

Para provar que você está à altura do desafio, sua gestora pediu para você criar um protótipo funcional. A ideia é simples: construir um *endpoint* (uma URL) que, ao ser acessado, devolva a lista de filmes disponíveis na plataforma.

Sua missão é usar o Flask para criar um servidor web simples que disponibilize um catálogo inicial de filmes no formato universal da internet: JSON.

## Mas tem um detalhe\! 
### Se o seu nome terminar com as letras A, H, L o seu serviço de streaming deve ter um design da cor Vermelha.
### Se o seu nome terminar com as letras E, O e Y o seu serviço de streaming deve ter um design da cor Azul.
### Se o seu nome terminar com as letras N, I, S (ou qualquer outra restante no alfabeto) o seu serviço de streaming deve ter um design da cor Roxa.

#### Acontece que a gestora percebeu muitos designs iguals e não chamou a atenção da direção. Por isso, a regra.

### 💡 O que é uma API e JSON?
Pense em uma **API** (Interface de Programação de Aplicações) como um garçom em um restaurante. Seu navegador ou aplicativo (o "cliente") faz um pedido para uma URL específica. O servidor Flask (a "cozinha") recebe esse pedido, prepara os dados e a API (o "garçom") entrega esses dados de volta para o cliente.

## 📋 Requisitos da Missão

Sua gestora precisa de um protótipo para apresentar aos investidores. Seu script Flask deve atender aos seguintes requisitos:

1.  **Servidor Flask:** O script deve iniciar um servidor web local.

2.  **Dados Fixos (Hardcoded):** Para este protótipo, a lista de filmes será criada diretamente no código Python. Deve ser uma lista de dicionários, onde cada dicionário representa um filme e possui as chaves: `id`, `titulo`, `diretor`, `genero`, `poster` e `ano`.

3.  **Crie uma rota (URLs):**
    * **URL:** `/filmes`
    * **Método:** `GET`
    * **Ação:** Deve retornar a lista JSON completa de filmes do catálogo.

    **Crie mais uma rota (URL)**
    * **URL:** `/`
    * **Métodos:** `GET`, `POST`
    * **Ação:** Deve retornar a página `index.html` com os filmes do catálogo.

4.  **Formato de Resposta:** A resposta da API **obrigatoriamente** deve ser no formato JSON. O Flask tem a função `jsonify` que faz exatamente isso.

5.  **Resultado Final:** Ao executar seu script e acessar `http://127.0.0.1:5000/filmes` em um navegador, a lista de filmes deve aparecer na tela, formatada como um texto JSON.

## 💡 Roteiro Sugerido para o Sucesso

Se não souber por onde começar, siga estes passos:

1.  **Importe as bibliotecas**: Você precisará de `Flask` e `jsonify` do pacote `flask`.
2.  **Crie a instância do Flask**: `app = Flask(__name__)`.
3.  **Crie seu catálogo de filmes**: Crie uma variável (ex: `filmes`) que seja uma lista de dicionários Python, com os dados de pelo menos 3 filmes diferentes.
4.  **Defina a rota**: Use o decorador `@app.route('/filmes')` para definir a URL do seu endpoint.
5.  **Crie a função da rota**: Defina uma função logo abaixo do decorador (ex: `get_filmes()`).
6.  **Retorne os dados em JSON**: Dentro da função, use `return jsonify(filmes)`. Isso converte sua lista Python para o formato JSON e a envia como resposta.
7.  **Inicie o servidor**: Use o bloco `if __name__ == '__main__':` para rodar sua aplicação com `app.run(debug=True)`.
8.  **Teste!** Rode seu script Python no terminal e acesse a URL no navegador para ver seu catálogo de filmes online!

Luz, câmera, ação... e código! 🎬
