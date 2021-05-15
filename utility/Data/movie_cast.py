# let's import all the packages we need
# requests: package used to query API and get the result back in Python
# json: package used to read and convert JSON format
# csv: package used to read and write csv
import requests, json, csv

# document all the parameters as variables
API_key = ""
# write a function to compose the query using the parameters provided
def get_data(API_key, Movie_ID):
    query = (
        "https://api.themoviedb.org/3/movie/"
        + str(Movie_ID)
        + "/credits?api_key="
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
    cast = []
    x = 0
    while x < 3 and x < len(dataset["cast"]):
        cast.append(dataset["cast"][x]["original_name"])
        x = x + 1
    i = 0
    Director = ""
    while i < len(dataset["crew"]):
        if dataset["crew"][i]["job"] == "Director":
            Director = dataset["crew"][i]["original_name"]
            break
        i = i + 1
    i = 0
    Producer = ""
    while i < len(dataset["crew"]):
        if (
            dataset["crew"][i]["job"] == "Producer"
            or dataset["crew"][i]["job"] == "Co-Producer"
        ):
            Producer = dataset["crew"][i]["original_name"]
            break
        i = i + 1
    Final_Cast = ""
    i = 0
    while x:
        Final_Cast = str(Final_Cast) + str(cast[i]) + " , "
        x = x - 1
        i = i + 1
    n=len(Final_Cast)
    Final_Cast=Final_Cast[:n-3]    
    result = [movie, Final_Cast, Director, Producer]
    # write data
    csvwriter.writerow(result)
    print(result)
    csvFile.close()


# write header to the file
csvFile = open("movie_collection_data_cast.csv", "a", encoding="utf-8", errors="ignore")
csvwriter = csv.writer(csvFile)
csvwriter.writerow(["ID", "Cast", "Director", "Producer"])
csvFile.close()
for movie in range(10000, 10600):
    text = get_data(API_key, movie)
    # make sure your process breaks when the pull was not successful
    # it's easier to debug this way
    if text == "error":
        continue
    write_file("movie_collection_data_cast.csv", text, movie)
