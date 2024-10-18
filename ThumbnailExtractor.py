import logging
import glob
import sqlite3

logger = logging.getLogger(__name__)

class ThumbnailExtractor:
    def __init__(self):
        pass

    def run(self, path, db_extension, image_extension):
        files = glob.glob(path + "/**/*" + db_extension, recursive=True)
        logger.info(f"{len(files)} {db_extension} file(s) found.")

        count = 0
        created_count = 0
        for file in files:
            count += 1
            image_file = file.replace(db_extension, image_extension)
            
            if glob.glob(image_file):
                logger.info(f"[-] [{count}/{len(files)}] [{image_file}] Image file already found. Skipped")
            else:
                try:
                    con = sqlite3.connect(file)
                    cursor = con.cursor()
                    cursor.execute("SELECT content FROM file_tree where filename == 'folder.jpg'")
                    data = cursor.fetchall()

                    with open(image_file, "wb") as f:
                        f.write(data[0][0])
                    logger.info(f"[o] [{count}/{len(files)}] [{image_file}] created")
                    created_count += 1

                except:
                    logger.warning(f"[x] [{count}/{len(files)}] [{file}] Fail to read. Skipped")

                finally:
                    con.close()
                    
        logger.info(f"{created_count} image file(s) created")

