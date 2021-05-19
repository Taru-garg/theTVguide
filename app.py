import os
import random
from pathlib import Path

import pyodbc
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request

from utility import searchCleaning
from utility.Database.python import conn
from utility.Database.python import SimpleSearch

# --------------------------------------------------------------------------------------------------------------------------------- #
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"
app = Flask(__name__)

# Connect to the Database
envPath = Path("utility/Database/.env")
load_dotenv(dotenv_path=envPath)

server = os.environ.get("SERVER")
database = os.environ.get("DATABASE")
username = os.environ.get("UID")
password = os.environ.get("PSWD")
port = os.environ.get("PORT")
driver = "{ODBC Driver 17 for SQL Server}"

cnxn = pyodbc.connect(
    "DRIVER="
    + driver
    + ";PORT=1433;SERVER="
    + server
    + ";PORT=1443;DATABASE="
    + database
    + ";UID="
    + username
    + ";PWD="
    + password
    + ";MARS_Connection=Yes"
)
# --------------------------------------------------------------------------------------------------------------------------------- #


@app.errorhandler(404)
def error():
    return render_template("error_page.html")


# --------------------------------------------------------------------------------------------------------------------------------- #


@app.route("/movie/<id>")
def movie(id):
    try:
        # make the query
        query = f"EXECUTE Data @movId= ? "
        query2 = f"EXECUTE fetchActors @movId= ? "

        # execute the query
        results = conn.processQuerySingle(conn.executeQuery(query, id, cnxn))
        results2 = conn.processQuerySingle(conn.executeQuery(query2, id, cnxn))

        return render_template(
            "movie.html",
            title=str(results["title"]),
            overview=str(results["overview"]),
            length=results["length"],
            director=results["Director"],
            ratings=results["ratings"],
            backdrop=IMAGE_BASE_URL + str(results["backdrop"]),
            poster=IMAGE_BASE_URL + str(results["poster"]),
            genre=str(results["genre"]),
            date=results["initial_release_date"],
            likes=results["likes"],
            stars=results2["Cast"].split(","),
        )
    except:
        return render_template("error_page.html")


# --------------------------------------------------------------------------------------------------------------------------------- #
@app.route("/search", methods=["POST"])
def searchInput():
    data = request.get_json()
    if data["data"] != "" and data["data"] != None and len(data["data"].strip()) >= 3:
        response = jsonify(
            data=SimpleSearch.SimpleSearch("%" + data["data"].strip() + "%", cnxn),
            status=200,
            mimetype="application/json",
        )
        return response
    else:
        response = jsonify(
            status=404,
            mimetype="application/json",
        )
        return response


# --------------------------------------------------------------------------------------------------------------------------------- #

@app.route("/search/go", methods=["POST"])
def searchEnter():
    # do sanitize one
    data = request.get_json()
    results = SimpleSearch.SimpleSearch(data["data"] + "%", cnxn)
    return dict(results)


# --------------------------------------------------------------------------------------------------------------------------------- #


@app.route("/")
def home():
    movId1 = random.randint(10000, 10300)
    movId2 = random.randint(10000, 10300)
    movId3 = random.randint(10000, 10300)
    # Queries
    query1 = f"EXECUTE Data @movId=?"
    query2 = f"EXECUTE Data @movId=?"
    query3 = f"EXECUTE Data @movId=?"

    # Getting the results
    results1 = conn.processQuerySingle(conn.executeQuery(query1, movId1, cnxn))
    results2 = conn.processQuerySingle(conn.executeQuery(query2, movId2, cnxn))
    results3 = conn.processQuerySingle(conn.executeQuery(query3, movId3, cnxn))

    return render_template(
        "index.html",
        movie1=[
            "/movie/" + str(results1["mov_id"]),
            results1["title"],
            IMAGE_BASE_URL + str(results1["backdrop"]),
            IMAGE_BASE_URL + str(results1["poster"]),
        ],
        movie2=[
            "/movie/" + str(results2["mov_id"]),
            results2["title"],
            IMAGE_BASE_URL + str(results2["backdrop"]),
            IMAGE_BASE_URL + str(results2["poster"]),
        ],
        movie3=[
            "/movie/" + str(results3["mov_id"]),
            results3["title"],
            IMAGE_BASE_URL + str(results3["backdrop"]),
            IMAGE_BASE_URL + str(results3["poster"]),
        ],
    )


# --------------------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    app.run(debug = True)
