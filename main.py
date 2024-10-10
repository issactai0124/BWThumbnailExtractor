# demo code for extracting thumbnail from bw file
import sqlite3

path = r"path of bw file" ### change this
image_file = path.replace(".bw", ".jpg")
con = sqlite3.connect(path)
cursor = con.cursor()
cursor.execute("SELECT content FROM file_tree where filename == 'folder.jpg'")
data = cursor.fetchall()
binary_data = data[0][0]

with open(image_file, "wb") as f:
    f.write(binary_data)