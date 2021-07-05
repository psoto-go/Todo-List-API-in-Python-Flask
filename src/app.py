from flask import Flask
app = Flask(__name__)
from flask import jsonify
from flask import request
import json

todos = [
    { "label": "My first task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    #llamo la informacion
    request_body = request.data 
    #paso la info en python
    decoded_object = json.loads(request_body)
    #se inserta el objeto en la lista
    todos.append(decoded_object)

    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    #delete el objeto en la position
    todos.pop(position)
    return jsonify(todos)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)