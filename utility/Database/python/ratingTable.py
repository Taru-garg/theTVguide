import itertools
import pandas as pd

# --------------------------------------------------------------------------------------------------------------------------------- #


def createInsertQueryRatings(filepath):
    ratingData = pd.read_csv(filepath, usecols=["ID", "Rating"])

    # Base Statement
    statement = "INSERT INTO RATINGS VALUES "

    for movID, rating in itertools.zip_longest(ratingData["ID"], ratingData["Rating"]):
        InsertQuery = statement + f"({movID}, {rating});\n"

        with open("utility/Database/sql/ratingTable.sql", "a+") as file:
            file.write(InsertQuery)


# --------------------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    filename = input("Enter file path:")
    createInsertQueryRatings(filename)
