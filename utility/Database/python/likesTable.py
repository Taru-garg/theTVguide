import itertools
import pandas as pd

# --------------------------------------------------------------------------------------------------------------------------------- #


def createInsertQueryRatings(filepath):
    likesData = pd.read_csv(filepath, usecols=["ID", "Likes"])

    # Base Statement
    statement = "INSERT INTO LIKES VALUES "

    for movID, likes in itertools.zip_longest(likesData["ID"], likesData["Likes"]):
        InsertQuery = statement + f"({movID}, {likes});\n"

        with open("utility/Database/sql/likesTable.sql", "a+") as file:
            file.write(InsertQuery)


# --------------------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    filename = input("Enter file path:")
    createInsertQueryRatings(filename)
