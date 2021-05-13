import requests, json, csv

API_key = ""

def get_data(API_key, Movie_ID):
    query = (
        "https://api.themoviedb.org/3/movie/"
        + str(Movie_ID)
        + "/reviews?api_key="
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
    Author = "" 
    Rating= None
    Content= ""
    if(len(dataset["results"])>0):
        Author=dataset["results"][0]["author"]
        Rating=dataset["results"][0]["author_details"]["rating"]
        Content=dataset["results"][0]["content"]
    result = [movie,Author,Rating,Content]
    csvwriter.writerow(result)
    print(result)
    csvFile.close()


csvFile = open("movie_collection_data_reviews.csv", "a", encoding="utf-8", errors="ignore")
csvwriter = csv.writer(csvFile)
csvwriter.writerow(["ID", "Author", "Rating", "Content"])
csvFile.close()
for movie in range(10000, 10600):
    text = get_data(API_key, movie)
    if text == "error":
        continue
    write_file("movie_collection_data_reviews.csv", text, movie)
