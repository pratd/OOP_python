import sqlite3


class SQLite:
    def __init__(self, file="application.db"):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


class NotFoundError(Exception):
    pass


class NotAuthorizedError(Exception):
    pass


def blog_lst_to_json(item):
    return {
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
    }


def fetch_blogs():
    try:
        with SQLite("application.db") as cur:
            # # connect to the database
            # con = sqlite3.connect('application.db')
            # cur = con.cursor()

            # execute the query
            cur.execute('SELECT * FROM blogs WHERE public=1 LIMIT 5')

            # Fetch the data and turn it into a dict
            result = list(map(blog_lst_to_json, cur.fetchall()))

            return result
    except Exception as e:
        print(e)
        return []

    # finally:
    #     # close the database
    #     con.close()


def fetch_blog(id: str):
    try:
        # connect to the database
        con = sqlite3.connect('application.db')
        cur = con.cursor()

        # execute the query
        cur.execute(f"SELECT * FROM blogs WHERE id='{id}'")
        result = cur.fetchone()

        if result is None:
            raise NotFoundError(f'Unable to find blog with id {id}.')

        data = blog_lst_to_json(result)
        if not data['public']:
            raise NotAuthorizedError(f'You are not allowed to access blog with id {id}.')
        return data
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundError(f'Unable to find blog with id {id}.')
    finally:
        # close the database
        con.close()

