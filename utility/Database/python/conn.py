def executeQuery(query, param, conn):
    cursor = conn.cursor()
    cursor.execute(query, param)
    return cursor


def processQuerySingle(cursor):
    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()
    cursor.close()
    results = dict(zip(columns, row))
    return results

def processQueryMultiple(cursor):
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    results = [dict(zip(columns, row)) for row in rows]
    cursor.close()
    return results