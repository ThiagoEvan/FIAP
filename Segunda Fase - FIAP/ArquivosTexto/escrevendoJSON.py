import json

dados = {
    "Thiago":{
        "Teleforne": "123456789",
        "Email": "email1@email.com"
        },

    "Lucas": {
        "Telefone": "987654321",
        "Email": "email2@email.com"
    }
}

arquivo_json = json.dumps(dados, indent= 2)

print(arquivo_json)