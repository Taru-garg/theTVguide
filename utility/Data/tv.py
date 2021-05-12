# let's import all the packages we need
# requests: package used to query API and get the result back in Python
# json: package used to read and convert JSON format
# csv: package used to read and write csv
import requests, json, csv, os

# document all the parameters as variables
API_key = ""
# write a function to compose the query using the parameters provided
def get_data(API_key, TV_ID):
    query = (
        "https://api.themoviedb.org/3/tv/"
        + str(TV_ID)
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


def write_file(filename, text, tv):
    dataset = json.loads(text)
    csvFile = open(filename, "a", encoding="utf-8", errors="ignore")
    csvwriter = csv.writer(csvFile)
    # unpack the result to access the "collection name" element
    try:
        no_of_episodes = dataset["number_of_episodes"]
    except:
        # for movies that don't belong to a collection, assign null
        no_of_episodes = None
    try:
        no_of_seasons = dataset["number_of_seasons"]
    except:
        # for movies that don't belong to a collection, assign null
        no_of_seasons = None
    try:
        backdrop_path = dataset["backdrop_path"]
    except:
        # for movies that don't belong to a collection, assign null
        backdrop_path = None
    try:
        poster_path = dataset["poster_path"]
    except:
        # for movies that don't belong to a collection, assign null
        poster_path = None
    try:
        genre = dataset["genres"][0]["name"]
    except:
        # for movies that don't belong to a collection, assign null
        genre = None
    try:
        overview = dataset["overview"]
    except:
        # for movies that don't belong to a collection, assign null
        overview = None
    try:
        first_air_date = dataset["first_air_date"]
    except:
        # for movies that don't belong to a collection, assign null
        first_air_date = None
    try:
        last_air_date = dataset["last_air_date"]
    except:
        # for movies that don't belong to a collection, assign null
        last_air_date = None
    result = [
        tv,
        dataset["original_name"],
        overview,
        genre,
        first_air_date,
        last_air_date,
        no_of_seasons,
        no_of_episodes,
        backdrop_path,
        poster_path,
    ]
    # write data
    csvwriter.writerow(result)
    print(result)
    csvFile.close()


# write header to the file
csvFile = open("TV_collection_data.csv", "a", encoding="utf-8", errors="ignore")
csvwriter = csv.writer(csvFile)
csvwriter.writerow(
    [
        "ID",
        "TV_show_name",
        "Overview",
        "Genres",
        "First_Air_Date",
        "Last_Air_Date",
        "number_of_seasons",
        "number_of_episodes",
        "backdrop_path",
        "poster_path",
    ]
)
csvFile.close()
for movie in range(10000, 10600):
    text = get_data(API_key, movie)
    # make sure your process breaks when the pull was not successful
    # it's easier to debug this way
    if text == "error":
        continue
    write_file("TV_collection_data.csv", text, movie)
