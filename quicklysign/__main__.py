from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def client():
    return send_from_directory("client/dist", "index.html")

@app.route("/<path:path>")
def base(path):
    return send_from_directory('client/dist', path)

# @app.route('/message')
# def generate_random():
#     args = request.args
#     print(args['name'])
#     return "Hello " + args['name']

if __name__ == '__main__':
    app.run()