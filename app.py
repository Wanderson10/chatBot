from flask import Flask, request, jsonify
import requests
import json
import re

app = Flask(__name__)

@app.route("/", methods=['POST'])
def main():
    data = request.get_json(silent=True)
  
    intentName = data['queryResult']['intent']['displayName']
    nome = data['queryResult']['parameters']['nome']
    prontuario = data['queryResult']['parameters']['prontuario']
    telefone = data['queryResult']['parameters']['telefone']

    


    if intentName != '' and nome !='' and prontuario !='' and telefone != '':
        
        response_data = {
            'fulfillmentMessages': [
                {
                    'text': {
                        'text': [f' Sr(a) {nome}, sua consulta foi marcada e seu prontuário é o {prontuario} e o seu telefone é {telefone}']
                    }
                }
            ]
        }
        return jsonify(response_data)

    

if __name__ == '__main__':
    app.debug = False
    app.run()