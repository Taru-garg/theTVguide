import numpy as np
import pandas as pd


def formatActorColumn(filepath):
    file = pd.read_csv(filepath)
    # Reading names of all the actors
    # Currently Unformatted
    cast = file["Cast"]

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


def createInsertQueryActor(filepath):
    cast = formatActorColumn(filepath)

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
        with open("utility/Database/actorTable.sql", "a+") as file:
            file.write(InsertQuery)
        actId = actId + 1


if __name__ == "__main__":
    file = input("Enter file Path: ")
    createInsertQueryActor(file)
