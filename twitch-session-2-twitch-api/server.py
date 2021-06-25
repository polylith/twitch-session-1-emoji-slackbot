from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_message():
    content = request.json
    print(content)
    if content.get("challenge"):
        return content.get("challenge")

    return jsonify({})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=5000)