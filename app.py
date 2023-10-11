from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para reiniciar as variáveis do usuário
def reiniciar_variaveis():
    user_data['estado'] = 'inicial'
    user_data['nome'] = None
    user_data['prontuario'] = None
    user_data['telefone'] = None

user_data = {
    'nome': None,
    'prontuario': None,
    'telefone': None,
    'estado': 'inicial'
}

@app.route("/", methods=['POST'])
def main():
    data = request.get_json(silent=True)
    user_message = data['queryResult']['queryText']
    response_data = {}

    if user_message == 'reiniciar':
        reiniciar_variaveis() 
        response_data['fulfillmentMessages'] = [
            {
                'text': {
                    'text': ['O processo foi reiniciado. Digite 1 para marcar uma consulta.']
                }
            }
        ]
    elif user_data['estado'] == 'inicial':
        if user_message == '1':
            user_data['estado'] = 'esperando_nome'
            response_data['fulfillmentMessages'] = [
                {
                    'text': {
                        'text': ['Ótimo! Por favor, digite seu nome.']
                    }
                }
            ]
        else:
            response_data['fulfillmentMessages'] = [
                {
                    'text': {
                        'text': ['Para marcar uma consulta, digite 1.']
                    }
                }
            ]
    elif user_data['estado'] == 'esperando_nome':
        if len(user_message) < 3:
            response_data['fulfillmentMessages'] = [
                {
                    'text': {
                        'text': ['Por favor, forneça um nome com pelo menos 3 caracteres.']
                    }
                }
            ]
        else:
            user_data['nome'] = user_message
            user_data['estado'] = 'esperando_prontuario'
            response_data['fulfillmentMessages'] = [
                {
                    'text': {
                        'text': ['Ótimo! Agora, por favor, digite seu prontuário.']
                    }
                }
            ]
    elif user_data['estado'] == 'esperando_prontuario':
        user_data['prontuario'] = user_message
        user_data['estado'] = 'esperando_telefone'
        response_data['fulfillmentMessages'] = [
            {
                'text': {
                    'text': ['Ótimo! Agora, por favor, digite seu número de telefone.']
                }
            }
        ]
    elif user_data['estado'] == 'esperando_telefone':
        user_data['telefone'] = user_message
        user_data['estado'] = 'finalizado'
        response_data['fulfillmentMessages'] = [
            {
                'text': {
                    'text': [f'Sr(a) {user_data["nome"]}, sua consulta foi marcada com sucesso. Seu prontuário é {user_data["prontuario"]} e seu telefone é {user_data["telefone"]}']
                }
            }
        ]
        reiniciar_variaveis()

    return jsonify(response_data)

if __name__ == '__main':
    app.debug = False
    app.run()
