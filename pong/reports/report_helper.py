from django.db import connection, transaction
import sqlite3
import os


def raw_sql_query(sql, injection = None):

    results = None
    try:
        with connection.cursor() as cursor:

            if injection:
                cursor.execute(sql, injection)
            else:
                cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
    except Exception as e:
        print(e)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        db = os.path.join(BASE_DIR, 'db.sqlite3')
        con = sqlite3.connect(db)

        with con:
            cursor = con.cursor()
            if injection:
                cursor.execute(sql, injection)
            else:
                cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

    return results