import recursos
from flask import Flask, jsonify

app = Flask(__name__)

API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"


#home:

@app.route('/')
def  home():
    return "Servidor está funcionando. Acesse /cotacao"

#cotacao:

@app.route('/cotacao', methods=['GET'])
def cotacao():

    try:
        response = request.get(API_URL)
        response.raise_for_status()

        dados_cotacao = response.json()

        cotacoes = {
            "dolar_real": {
                "nome": dados_cotacao['USDBRL']['name'],
                "valor": dados_cotacao['USDBRL']['bid'],
                "atualizado_em": dados_cotacao['USDBRL']['create_date']
                },
            "euro_real":{
                "nome": dados_cotacao['EURBRL']['name'],
                "valor": dados_cotacao['EURBRL']['bid'],
                "atualizado_em": dados_cotacao['EURBRL']['create_date']
            },
            "bitcoin_real": {
                "nome": dados_cotacao['BTCBRL']['name'],
                "valor": dados_cotacao['BTCBRL']['bid'],
                "atualizado_em": dados_cotacao['BTCBRL']['create_date']
            }
            
            return jsonify(cotacoes),200

    except:
        request.exception.RequestException as e:
    