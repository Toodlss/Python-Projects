import sqlite3
conn = sqlite3.connect("files.db")
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        filename TEXT)")
    conn.commit()

conn = sqlite3.connect("files.db")

fileList =('information.docx', 'Hello.txt', 'myImage.png',
           'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in the tuple to find the names that end in y.
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # The value for each row will be one name out of the tuple therefore (x,)
            # will denote a one element tuple for each name ending with y.
            cur.execute("INSERT INTO tbl_files (filename) VALUES (?)", (x,))
            print(x)

conn.close()
