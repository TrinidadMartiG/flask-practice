from flask import Flask, request, render_template, jsonify
# with these properties above i can receive info and render html document

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        return render_template('index.html')
    else:
        return jsonify({
            "mensaje": "this is a json post response"
        })


@app.route("/ping", methods=['POST'])
def pingpong():
    body = request.get_json()
    response = {
        "mensaje": body["name"] + " ha decidido jugar pingpong"
    }
    return jsonify(response)


@app.route("/saludar/<nombre>", methods=['GET'])
def saludar(nombre): #este codigo crea una funcion que recibe como argumento y es utilizado por la funcion
    return "Hola! "+ nombre


app.run(host = '0.0.0.0')
