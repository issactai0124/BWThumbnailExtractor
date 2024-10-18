import logging
from time import localtime, strftime, mktime
from datetime import timedelta
from ConfigReader import ConfigReader
from ThumbnailExtractor import ThumbnailExtractor

ver = "0.21"
logger = logging.getLogger(__name__)
start_time = localtime()
logfile = f"bwExtract_v{ver}_{strftime('%Y%m%d%H%M%S', start_time)}.log"
logging.basicConfig(filename=logfile, level=logging.INFO)

def main():
    logger.info(f" [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] BW Thumbnail Extractor ver{ver} started")
    
    config = ConfigReader()
    try:
        config.run()
        logger.info(f"Target path = {config.path}")

        extractor = ThumbnailExtractor()
        extractor.run(config.path, config.dbExtension, config.imageExtension)
    except Exception as error:
        logger.error(error)

    end_time = localtime()
    logger.info(f" [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] Program ran successfully")
    logger.info(f" [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] Running time = {timedelta(seconds= mktime(end_time) - mktime(start_time))}")

if __name__ == '__main__':
    main()