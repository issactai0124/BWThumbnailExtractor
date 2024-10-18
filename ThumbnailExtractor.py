import LogUtil
import glob
import sqlite3
import os

class ThumbnailExtractor:
    def __init__(self):
        pass

    def run(self, path, db_extension, image_extension):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Folder [{path}] not found!")

        files = glob.glob(path + "/**/*" + db_extension, recursive=True)
        LogUtil.info(f"{len(files)} {db_extension} file(s) found")

        count = 0
        created_count = 0
        for file in files:
            count += 1
            image_file = file.replace(db_extension, image_extension)
            
            if glob.glob(image_file):
                LogUtil.info(f"[-] [{count}/{len(files)}] [{image_file}] Image file already found. Skipped")
            else:
                try:
                    LogUtil.info(f"[ ] [{count}/{len(files)}] About to load BW file [{file}]...")
                    con = sqlite3.connect(file)
                    cursor = con.cursor()
                    cursor.execute("SELECT content FROM file_tree where filename == 'folder.jpg'")
                    data = cursor.fetchall()

                    with open(image_file, "wb") as f:
                        f.write(data[0][0])
                    LogUtil.info(f"[o] [{image_file}] created")
                    created_count += 1

                except:
                    LogUtil.warning(f"[x] Fail to read. Skipped")

                finally:
                    con.close()
                    
        LogUtil.info(f"{created_count} image file(s) created")

