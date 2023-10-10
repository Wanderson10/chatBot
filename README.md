# ChatBot de Agendamento Médico

### Visão Geral das Tecnologias Utilizadas

O projeto "ChatBot de Agendamento Médico" combina várias tecnologias para criar um sistema automatizado de agendamento médico. Abaixo, apresentamos uma visão geral das principais tecnologias e suas funções no projeto:

Dialogflow:

Função: O Dialogflow, do Google, é uma plataforma de processamento de linguagem natural que permite a comunicação entre o chatbot e os usuários por meio de texto ou voz.
Uso no Projeto: O Dialogflow é usado para interpretar as mensagens dos usuários, extrair intenções e parâmetros e gerar respostas personalizadas.

Flask:

Função: Flask é um framework de desenvolvimento web em Python que serve como servidor para a aplicação.
Uso no Projeto: O Flask é usado para criar e hospedar o servidor que lida com as solicitações do Dialogflow e executa as ações necessárias, como agendar consultas médicas.
Ngrok:

Função: O Ngrok é uma ferramenta que permite expor um servidor localmente em um URL público temporário.
Uso no Projeto: O Ngrok é usado para tornar o servidor Flask localmente executado acessível online, permitindo que o Dialogflow se comunique com a aplicação Flask em execução.

AutoResponderWA:

Função: O AutoResponderWA é um aplicativo que permite a interação com o WhatsApp usando chatbots.
Uso no Projeto: O AutoResponderWA é utilizado para vincular o chatbot do Dialogflow ao WhatsApp, possibilitando que os usuários agendem consultas médicas enviando mensagens para um número de telefone específico.
Ambiente Virtual Python:

Função: Um ambiente virtual Python é usado para isolar as dependências do projeto e garantir que ele seja executado com as versões corretas das bibliotecas.
Uso no Projeto: É criado um ambiente virtual Python para instalar e gerenciar as dependências do projeto, garantindo que ele seja portátil e independente do sistema host.
Estas tecnologias trabalham em conjunto para criar uma solução completa de agendamento médico automatizado que permite aos usuários agendar consultas de forma conveniente por meio de mensagens de texto no WhatsApp.

## Como Testar

Você pode testar o chatbot enviando uma mensagem para o número de telefone: +55 51 997866074.

## Como Replicar o Projeto

Se deseja replicar a aplicação em sua máquina e testá-la com seu número de telefone de preferência, siga os passos abaixo:

### 1. Crie seu Ambiente Virtual

```

Primeiro, crie um ambiente virtual com os seguintes comandos:

```
python -m venv nome_do_ambiente_virtual

### 2. Ative o Ambiente Virtual

``` 

No Linux:

source nome_do_ambiente_virtual/bin/activate

No Windows:

nome_do_ambiente_virtual\Scripts\Activate

```

### 3. Instale as Dependências
Ative o ambiente virtual e, em seguida, instale as dependências a partir do arquivo requirements.txt:

```
pip install -r requirements.txt

```

### 4. Configuração do Dialogflow

```
A configuração do Dialogflow é essencial para definir a interação entre o chatbot e o usuário. Siga estas etapas:

Crie um projeto no Dialogflow.

No Console do Dialogflow, crie uma intenção que você deseja usar para interagir com o chatbot.

Configure a ação da intenção para a ação que deseja que seu aplicativo Flask execute.

Treine seu modelo de linguagem natural com frases de exemplo para a intenção.

Implante seu modelo para aplicá-lo.

Anote o nome do projeto e a chave de acesso do projeto para uso posterior.

```
### 5. Configuração do Ngrok e Flask
```

rode seu servidor flask : 

flask run 

O Ngrok é usado para expor seu servidor Flask localmente em um URL público. Siga estas etapas para configurar o Ngrok:

acesse esse endereço : https://dashboard.ngrok.com/get-started/setup e faça o login e abtenha o seu token.

Abra o terminal e navegue até o diretório onde você extraiu o Ngrok.

Execute o seguinte comando para iniciar o Ngrok e gerar um túnel para a porta em que seu aplicativo Flask está em execução (por exemplo, porta 5000):

no terminal rode o seguinte comando : 

ngrok authtoken SEU_TOKEN_AQUI

em seguida : 
ngrok http 5000


O Ngrok exibirá uma saída que inclui uma URL pública temporária que você pode usar para acessar seu aplicativo Flask online.

Anote a URL pública gerada pelo Ngrok, que será semelhante a https://random-letters-and-numbers.ngrok.io.



```

### 6. Vinculando seu Aplicativo Flask ao Dialogflow

```
Para vincular seu aplicativo Flask ao Dialogflow, siga estas etapas:

No Console do Dialogflow, vá para as Configurações do Projeto.

Clique na guia Conexões.

Clique em Criar uma Conexão.

Escolha a integração "Webhook".

Cole a URL pública do Ngrok (a URL gerada anteriormente) no campo "URL do webhook".

Salve as configurações.

No Console do Dialogflow, vá para a seção "Fulfillment".

Ative a opção "Webhook".

Cole a URL pública do Ngrok na seção "URL do Webhook".

Configure outros detalhes do webhook conforme necessário.

Salve as configurações do webhook.

Seu aplicativo Flask agora está vinculado ao Dialogflow e pode receber solicitações do chatbot.

```

## 7. Vinculando a Chave do Dialogflow ao AutoResponderWA

```
Para permitir que o AutoResponderWA se comunique com o Dialogflow, siga estas etapas:

Baixe o AutoResponderWA e siga as instruções de instalação do projeto.

Abra o AutoResponderWA e navegue até as configurações de integração.

Encontre a seção "Integração com Dialogflow" e insira a chave de acesso que você obteve ao configurar o projeto no Dialogflow.

Certifique-se de que o AutoResponderWA esteja configurado para encaminhar as mensagens recebidas para o Dialogflow e receber as respostas correspondentes.

Salve as configurações e verifique se o AutoResponderWA está online e pronto para receber mensagens no número de telefone configurado.

Agora, seu chatbot está vinculado ao AutoResponderWA e pode responder às mensagens recebidas no número de telefone especificado, utilizando o Dialogflow para processamento de linguagem natural. Certifique-se de testar a integração para garantir que tudo esteja funcionando conforme o esperado.

```