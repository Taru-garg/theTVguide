import requests, json, csv

API_key = ""


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
        array = response.json()
        text = json.dumps(array)
        return text
    else:
        return "error"


def write_file(filename, text, movie):
    dataset = json.loads(text)
    csvFile = open(filename, "a", encoding="utf-8", errors="ignore")
    csvwriter = csv.writer(csvFile)
    try:
        Rating = dataset["vote_average"]
    except:
        Rating = None
    try:
        Likes = dataset["vote_count"]
    except:
        Likes = None
    result = [movie, Rating, Likes]
    csvwriter.writerow(result)
    print(result)
    csvFile.close()


csvFile = open(
    "movie_collection_data_reviews.csv", "a", encoding="utf-8", errors="ignore"
)
csvwriter = csv.writer(csvFile)
csvwriter.writerow(["ID", "Rating", "Likes"])
csvFile.close()
for movie in range(10000, 10600):
    text = get_data(API_key, movie)
    if text == "error":
        continue
    write_file("movie_collection_data_reviews.csv", text, movie)
