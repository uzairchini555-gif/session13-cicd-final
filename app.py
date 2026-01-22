from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "session 13 App version 1.1 - ae kash madiney mein mjhey maut yun ae"
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)

