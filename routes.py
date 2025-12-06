import requests 
from flask import Blueprint, jsonify

API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

app_routes = Blueprint('cotacao', __name__)

@app_routes.route('/cotacao', methods=['GET'])
def cotacao():
    
    try:
       
        response = requests.get(API_URL) 
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
        }
        return jsonify(cotacoes), 200

    except requests.exceptions.RequestException as e: 
        return jsonify({"erro": f"Falha ao buscar cotação da API externa: {e}"}), 500
    
    except Exception as e: 
        return jsonify({"erro": f"Ocorreu um erro do servidor: {e}"}), 500