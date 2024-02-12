from flask import Flask, send_from_directory
from api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def home():
	return send_from_directory("client/dist", "index.html")


@app.route("/<path:path>")
def base(path):
	return send_from_directory('client/dist', path)


if __name__ == "__main__":
	# print out all available routes
	for rule in app.url_map.iter_rules():
		print(rule)

	app.run(host="127.0.0.1", port=8080, debug=True)