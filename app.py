from flask import Flask, render_template, request, jsonify, redirect
from flask.templating import render_template_string
from utility import searchCleaning

app = Flask(__name__)


@app.route("/movie/<id>")
def movie(id):
    print(id)
    return render_template("movie.html")


@app.route("/search", methods=["POST"])
def searchInput():
    data = request.get_json()
    # print(data)
    response = jsonify(
        data=searchCleaning.sanitize(data["data"]),
        status=200,
        mimetype="application/json",
    )
    return response


@app.route("/search/go", methods=["POST"])
def searchEnter():
    data = request.get_json()
    # print(data)
    return redirect("/")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
