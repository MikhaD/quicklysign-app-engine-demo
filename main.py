from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def client():
    return send_from_directory("client/dist", "index.html")

@app.route("/<path:path>")
def base(path):
    return send_from_directory('client/dist', path)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)