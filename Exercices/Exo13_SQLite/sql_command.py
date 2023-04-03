import sqlite3


def creation_todo():
    conn = None
    try:
        conn = sqlite3.connect('todo.sqlite')
        cur = conn.cursor()
        cur.execute(''' DROP TABLE IF EXISTS todo
                    ''')
        cur.execute(''' CREATE TABLE IF NOT EXISTS todo(
                            id integer PRIMARY KEY, 
                            name TEXT, 
                            description TEXT);
                    ''')
        return conn
    except OSError as e:
        print(e)


def add_task(conn, task):
    sql = ''' INSERT INTO todo(name, description)
              VALUES (?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def delete_task(conn, task):
    sql = ''' DELETE FROM todo WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def select(conn):
    sql = ''' SELECT * FROM todo '''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def close(conn):
    conn.close()


def update_description(conn, task, nv_task):
    sql = ''' UPDATE todo SET description = ? WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (task, nv_task))
    conn.commit()
    return cur.lastrowid


def update_name(conn, task, nv_nom):
    sql = ''' UPDATE todo SET name  = ? WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (task, nv_nom))
    conn.commit()
    return cur.lastrowid