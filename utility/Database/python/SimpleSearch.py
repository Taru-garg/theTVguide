import utility.Database.python.conn as con


def SimpleSearch(param, conn):
    queryActor = "Select mov_id, title from movies where lower(title) like lower(?)"
    result = con.processQueryMultiple(con.executeQuery(queryActor, param, conn))
    return result
