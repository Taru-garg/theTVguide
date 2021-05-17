def executeQuery(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor


def processQuerySingle(cursor):
    columns = [column[0] for column in cursor.description]
    results = dict(zip(columns, cursor.fetchone()))
    return results
