# let's import all the packages we need
# requests: package used to query API and get the result back in Python
# json: package used to read and convert JSON format
# csv: package used to read and write csv
from typing_extensions import runtime
import requests, json, csv, os

# document all the parameters as variables
API_key = ""
# write a function to compose the query using the parameters provided
def get_data(API_key, Movie_ID):
    query = (
        "https://api.themoviedb.org/3/movie/"
        + str(Movie_ID)
        + "?api_key="
        + API_key
        + "&language=en-US"
    )
    response = requests.get(query)
    if response.status_code == 200:
        # status code ==200 indicates the API query was successful
        array = response.json()
        text = json.dumps(array)
        return text
    else:
        return "error"


def write_file(filename, text, movie):
    dataset = json.loads(text)
    csvFile = open(filename, "a", encoding="utf-8", errors="ignore")
    csvwriter = csv.writer(csvFile)
    # unpack the result to access the "collection name" element
    try:
        collection_name = dataset["belongs_to_collection"]["name"]
    except:
        # for movies that don't belong to a collection, assign null
        collection_name = None
    try:
        backdrop_path = dataset["backdrop_path"]
    except:
        backdrop_path = None
    try:
        poster_path = dataset["poster_path"]
    except:
        backdrop_path = None
    try:
        genre = dataset["genres"][0]["name"]
    except:
        genre = None
    try:
        overview = dataset["overview"]
    except:
        overview = None
    try:
        release = dataset["release_date"]
    except:
        release = None
    try:
        Runtime = dataset["runtime"]
    except:
        Runtime = None    
    result = [
        movie,
        dataset["original_title"],
        overview,
        genre,
        release,
        collection_name,
        backdrop_path,
        poster_path,
        Runtime,
    ]
    # write data
    csvwriter.writerow(result)
    print(result)
    csvFile.close()


# write header to the file
csvFile = open("movie_collection_data.csv", "a", encoding="utf-8", errors="ignore")
csvwriter = csv.writer(csvFile)
csvwriter.writerow(
    [
        "ID",
        "Movie_name",
        "Overview",
        "Genres",
        "Release Date",
        "Collection_name",
        "backdrop_path",
        "poster_path",
        "Runtime",
    ]
)
csvFile.close()
for movie in range(10000, 10600):
    text = get_data(API_key, movie)
    # make sure your process breaks when the pull was not successful
    # it's easier to debug this way
    if text == "error":
        continue
    write_file("movie_collection_data.csv", text, movie)
