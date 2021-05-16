from flask import Flask, jsonify, redirect, render_template, request
import time
import random
from utility import searchCleaning
from utility.Database.python import conn

# --------------------------------------------------------------------------------------------------------------------------------- #
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"
app = Flask(__name__)

# --------------------------------------------------------------------------------------------------------------------------------- #


@app.errorhandler(500)
def error():
    return render_template("error_page.html")


@app.route("/movie/<id>")
def movie(id):
    try:
        # make the query
        query = f"EXECUTE Data @movId={int(id)}"
        # execute the query
        cursor = conn.exectueQuery(query)
        # extract the columns
        columns = [column[0] for column in cursor.description]
        # fetch the row and make dict
        results = dict(zip(columns, cursor.fetchone()))
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
        )
    except:
        return render_template("error_page.html")


# --------------------------------------------------------------------------------------------------------------------------------- #


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


# --------------------------------------------------------------------------------------------------------------------------------- #


@app.route("/search/go", methods=["POST"])
def searchEnter():
    data = request.get_json()
    # print(data)
    return redirect("/")


# --------------------------------------------------------------------------------------------------------------------------------- #


@app.route("/")
def home():
    movId1 = random.randint(10000, 10300)
    movId2 = random.randint(10000, 10300)
    movId3 = random.randint(10000, 10300)
    # Queries
    query1 = f"EXECUTE Data @movId={movId1}"
    query2 = f"EXECUTE Data @movId={movId2}"
    query3 = f"EXECUTE Data @movId={movId3}"
    
    # Getting the results
    cursor1 = conn.exectueQuery(query1)
    time.sleep(5)
    cursor2 = conn.exectueQuery(query2)
    time.sleep(5)
    cursor3 = conn.exectueQuery(query3)
    time.sleep(5)

    # Extracting Columns
    columns = [column[0] for column in cursor1.description]
    # Mapping columns to dict
    results1 = dict(zip(columns, cursor1.fetchone()))
    results2 = dict(zip(columns, cursor2.fetchone()))
    results3 = dict(zip(columns, cursor3.fetchone()))

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
    app.run(debug=True,threaded=False)
