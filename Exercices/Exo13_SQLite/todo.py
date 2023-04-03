import sql_command as sql

conn = sql.creation_todo()

# add todo in table
add_todo = ("todo1", "description todo 1")
add_todo2 = ("todo2", "description todo 2")
sql.add_task(conn, add_todo)
sql.add_task(conn, add_todo2)

sql.select(conn)
print("___________________")

sql.update_description(conn, 1, "nouv todo description 1")
sql.select(conn)

print("___________________")
sql.update_name(conn, 1, "nouv todo 1")
sql.select(conn)


sql.close(conn)