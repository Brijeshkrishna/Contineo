from flask import Flask, render_template

app = Flask(__name__, template_folder="template", static_folder="static")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
