import itertools
from os import stat
import numpy as np
import pandas as pd

# --------------------------------------------------------------------------------------------------------------------------------- #

def formatColumn(filepath, column):
    file = pd.read_csv(filepath)
    # Reading names of all the actors
    # Currently Unformatted
    cast = file[column]

    # Formatting the Cast Column
    # further we only need unique names
    FormattedCast = [
        [x.strip().replace("'", "") for x in people.split(",")] for people in cast
    ]

    # with numpy we have an elegant solution
    # np.unique function not only selects unique
    # data from array but also array of arrays
    npFormattedCast = np.array(FormattedCast)
    npFormattedCast = np.unique(npFormattedCast)
    return npFormattedCast

# --------------------------------------------------------------------------------------------------------------------------------- #

def createInsertQueryActor(filepath):
    cast = formatColumn(filepath, 'Cast')

    # Base statement
    statement = "INSERT INTO ACTOR VALUES "

    actId = 1
    for people in cast:
        name = people.split(' ', 1)
        if len(name) > 1:
            InsertQuery = statement + f"({actId}, '{name[0]}', '{name[1]}', NULL, NULL);\n"
        
        # This step has to be done as sometimes actor might not have a last name
        else :
            InsertQuery = statement + f"({actId}, '{name[0]}', NULL, NULL, NULL);\n"
        
        with open("utility/Database/sql/actorTable.sql", "a+") as file:
            file.write(InsertQuery)
        actId = actId + 1


# --------------------------------------------------------------------------------------------------------------------------------- #

def createInsertQueryDirector(filepath):
    Directors = formatColumn(filepath, 'Director')

    # Base statement
    statement = "INSERT INTO DIRECTOR VALUES "

    dirId = 1
    for people in Directors:
        name = people.split(' ', 1)
        if len(name) > 1:
            InsertQuery = statement + f"({dirId}, '{name[0]}', '{name[1]}', NULL, NULL);\n"
        
        # This step has to be done as sometimes director might not have a last name
        else :
            InsertQuery = statement + f"({dirId}, '{name[0]}', NULL, NULL, NULL);\n"
        
        with open("utility/Database/sql/directorTable.sql", "a+") as file:
            file.write(InsertQuery)
        dirId = dirId + 1

# --------------------------------------------------------------------------------------------------------------------------------- #

def createInsertQueryDirection(filepath):
    directors = formatColumn(filepath, 'Director')
    otherData = pd.read_csv(filepath, usecols=['ID', 'Director'])
    directorsUnformatted = otherData['Director']
    
    dirTodirId = [np.searchsorted(directors,director)+1 for director in directorsUnformatted]
    # Base statement
    statement = "INSERT INTO DIRECTION VALUES "

    for movID, dirID in itertools.zip_longest(otherData['ID'], dirTodirId):
        InsertQuery = statement + f'({movID},{dirID});\n'
        with open("utility/Database/sql/directionTable.sql", "a+") as file:
            file.write(InsertQuery)

# --------------------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    file = input("Enter file Path: ")
    createInsertQueryActor(file)
    createInsertQueryDirector(file)
    createInsertQueryDirection(file)
