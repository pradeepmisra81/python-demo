from flask import Flask, jsonify, request,send_file

app = Flask()
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
@app.route('/my-first-api', methods = ['GET'])
def hello():

    name = request.args.get('name')

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text
