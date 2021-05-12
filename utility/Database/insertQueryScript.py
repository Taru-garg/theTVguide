import pandas as pd
import numpy as np

#Use for movie_collection_data.csv file
def CreateInsertQuery(filename):
    Movie_data = pd.read_csv(filename)
    Movie_data = np.array(Movie_data)

    print("Input data has %s rows" %Movie_data.shape[0] + " and %s columns" %Movie_data.shape[1])

    #Table : MOVIES 
    #we need values of 1st,2nd,3rd and 5th column currently
    attributesM = [0,1,2,4]

    statement = "INSERT INTO MOVIES VALUES "
    for i in range(5):   #replace 5 with Movie_data.shape[0] (number of records)
        statement += '('
        for j in attributesM:
            if pd.isnull(Movie_data[i,j]):
                s = "NULL"
            else:
                s = "'" + "%s" %Movie_data[i,j] + "'"
            statement += s + ','
        statement = statement.rstrip(',')
        statement += '),'
    statement = statement.rstrip(',')
    statement += ';'
    print('\n')
    print(statement)

    #Table : GENRE
    attributesG = [3]  #gen_id is not present currently #add index of gen_id HERE
    statement = "INSERT INTO GENRES VALUES "
    for i in range(15):   #replace 15 with Movie_data.shape[0] (number of records)
        statement += '('
        for j in attributesG:
            if pd.isnull(Movie_data[i,j]):
                s = "NULL"
            else:
                s = "'" + "%s" %Movie_data[i,j] + "'"
            statement += s + ','
        statement = statement.rstrip(',')
        statement += '),'
    statement = statement.rstrip(',')
    statement += ';'
    print('\n')
    print(statement)

    #Table : movieImageData
    attributesMI = [0,6,7]
    statement = "INSERT INTO movieImageData VALUES "
    for i in range(5):   #replace 5 with Movie_data.shape[0] (number of records)
        statement += '('
        for j in attributesMI:
            if pd.isnull(Movie_data[i,j]):
                s = "NULL"
            else:
                s = "'" + "%s" %Movie_data[i,j] + "'"
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




