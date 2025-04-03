from time import strptime

from flask import Flask, jsonify
from datetime import date, datetime

app = Flask(__name__)


@app.route('/hoje/<data>')
def valores_hoje(data):
    try:
        data_inserida = datetime.strptime(data, '%d-%m-%Y')
        hoje = datetime.today()
        print(data_inserida)
        situacao = hoje - data_inserida
        print(hoje)
        print(situacao)
        if situacao.days < 0:
            status = 'futuro'
            mensagem = 'A data inserida esta no futuro'
        elif situacao.days > 0:
            status = 'passado'
            mensagem = 'A data inserida esta no passado'
        else:
            status = 'presente'
            mensagem = 'A data inserida eh a data atual'

        return jsonify({"mensagem": mensagem,
                        "status": status,
                        "data_atual": hoje,
                        "data_inserida": data_inserida,
                        "variacao_dias": abs(situacao.days),
                        "variacao_mes": abs(situacao.days) // 30,
                        "variacao_ano": abs(situacao.days) // 365,
                        })

    except ValueError:
        return jsonify({"erro": "Data incorreta"})
    except TypeError:
        return jsonify({"erro": "Data incorreta."})

    # return jsonify({'message': 'Hello World!'})


if __name__ == '__main__':
    app.run(debug=True)
