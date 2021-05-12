import pandas as pd
import numpy as np

#Use for movie_collection_data.csv file
def CreateInsertQuery(filename):
    Movie_data = pd.read_csv(filename)

    print("Input data has %s rows" %Movie_data.shape[0] + " and %s columns" %Movie_data.shape[1])

    #Table : MOVIES 
    attributesM = ["ID","Movie_name","Overview","Release Date"] #required attributes [for now]
    statement = "INSERT INTO MOVIES VALUES "
    for i in range(5):   #replace 5 with Movie_data.shape[0] (number of records)
        statement += '('
        for j in attributesM:
            if pd.isnull(Movie_data[j][i]):
                s = "NULL"
            else:
                s = "'" + "%s" %Movie_data[j][i] + "'"
            statement += s + ','
        statement = statement.rstrip(',')
        statement += '),'
    statement = statement.rstrip(',')
    statement += ';'
    print('\n')
    print(statement)

    #Table : GENRE
    attributesG = ["Genres"]  #gen_id is not present currently 
    statement = "INSERT INTO GENRES VALUES "
    for i in range(15):   #replace 15 with Movie_data.shape[0] (number of records)
        statement += '('
        for j in attributesG:
            if pd.isnull(Movie_data[j][i]):
                s = "NULL"
            else:
                s = "'" + "%s" %Movie_data[j][i] + "'"
            statement += s + ','
        statement = statement.rstrip(',')
        statement += '),'
    statement = statement.rstrip(',')
    statement += ';'
    print('\n')
    print(statement)

    #Table : movieImageData
    attributesMI = ["ID","backdrop_path","poster_path"]  #required attributes 
    statement = "INSERT INTO movieImageData VALUES "
    for i in range(5):   #replace 5 with Movie_data.shape[0] (number of records)
        statement += '('
        for j in attributesMI:
            if pd.isnull(Movie_data[j][i]):
                s = "NULL"
            else:
                s = "'" + "%s" %Movie_data[j][i] + "'"
            statement += s + ','
        statement = statement.rstrip(',')
        statement += '),'
    statement = statement.rstrip(',')
    statement += ';'
    print('\n')
    print(statement)


if __name__=="__main__":
    filename = input("Enter file path:")
    CreateInsertQuery(filename)




