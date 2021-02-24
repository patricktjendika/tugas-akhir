from flask_ngrok import run_with_ngrok
from flask import Flask, render_template
app = Flask(__name__)

run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def index():
    return "<h1>Running Flask on Google Colab WAW!</h1>"

@app.route("/test/<param>")
def test(param):
  return "<h1>Hello "+param+"!</h1>"

@app.route("/template")
def template():
  return render_template("index.html")

if __name__ == "__main__":
    app.run()