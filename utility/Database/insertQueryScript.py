import numpy as np
import pandas as pd


def createInsertQueryGenres(filename):
    # Read the Data from the file provided
    movieData = pd.read_csv(filename)

    # Base Insert statement
    statement = "INSERT INTO GENRES VALUES "

    # Fetching all the unique Genres from the Genres Column Ignoring the null vals
    uniqueGenres = movieData['Genres'].dropna().unique()
    genId = 1

    # Make Query and insert it into a .sql file
    for genre in uniqueGenres:
        InsertQuery = statement + f"({genId}, '{genre}');\n"
        with open('utility/Database/genreTable.sql', 'a+') as file:
            file.write(InsertQuery)
        genId = genId + 1

def createInsertQueryMovies(filename):
    Movie_data = pd.read_csv(filename)
    #print("[INFO] Input data has %s rows" %Movie_data.shape[0] + " and %s columns" %Movie_data.shape[1])
    Movie_data = Movie_data.dropna(axis=0,how="all") #drop null records
    attributesM = ["ID","Movie_name","Overview","Release Date"] #required attributes [for now]
    statement = "INSERT INTO MOVIES VALUES "
    for i in range(Movie_data.shape[0]):
        values = '(' 
        for j in attributesM:
            if pd.isnull(Movie_data[j][i]):
                values += "NULL,"
            else:
                values += f"'{Movie_data[j][i]}',"
        values = values.rstrip(',')
        values += ");\n"
        query = statement + values
        with open('utility/Database/moviesTable.sql', 'a+') as file:
            file.write(query)

def createInsertQueryImages(filename):
    image_data = pd.read_csv(filename)
    image_data = image_data.dropna(axis=0,how="all") #drop null records
    attributesMI = ["ID","backdrop_path","poster_path"]  #required attributes 
    statement = "INSERT INTO movieImageData VALUES "
    for i in range(image_data.shape[0]):
        values = '(' 
        for j in attributesMI:
            if pd.isnull(image_data[j][i]):
                values += "NULL,"
            else:
                values += f"'{image_data[j][i]}',"
        values = values.rstrip(',')
        values += ");\n"
        query = statement + values
        with open('utility/Database/movieImageTable.sql', 'a+') as file:
            file.write(query)
            


if __name__=="__main__":
    filename = input("Enter file path:")
    createInsertQueryGenres(filename)
    createInsertQueryMovies(filename)
    createInsertQueryImages(filename)




