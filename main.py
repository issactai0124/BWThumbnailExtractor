import LogUtil
from ConfigReader import ConfigReader
from ThumbnailExtractor import ThumbnailExtractor
import sys

def main():
    LogUtil.start()
    
    config = ConfigReader()
    try:
        config.run()
        LogUtil.info(f"Target path = [{config.path}]")

        extractor = ThumbnailExtractor()
        extractor.run(config.path, config.dbExtension, config.imageExtension)
    except Exception as error:
        LogUtil.error(error)
        return 1

    LogUtil.finish()
    return 0

if __name__ == '__main__':
    sys.exit(main())