from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        peso = float(request.form['peso'])
        altura_cm = float(request.form['altura'])
        altura_m = altura_cm / 100

        imc = peso / (altura_m ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        return render_template(
            'resultado.html',
            imc=f"{imc:.2f}",
            classificacao=classificacao
        )

    except ValueError:
        return render_template('resultado.html', imc="Inválido", classificacao="Dados incorretos")

if __name__ == '__main__':
    app.run(debug=True)