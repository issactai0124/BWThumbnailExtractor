import logging
from time import gmtime, strftime, mktime
from datetime import timedelta
from ConfigReader import ConfigReader
from ThumbnailExtractor import ThumbnailExtractor

ver = "0.20"
logger = logging.getLogger(__name__)
start_time = gmtime()
logfile = f"bwExtract_v{ver}_{strftime('%Y%m%d%H%M%S', start_time)}.log"
logging.basicConfig(filename=logfile, level=logging.INFO)

def main():
    logger.info(f"BW Thumbnail Extractor ver{ver} started at {strftime('%Y-%m-%d %H:%M:%S', start_time)}")
    
    config = ConfigReader()
    try:
        config.run()
        logger.info(f"Target path = {config.path}")

        extractor = ThumbnailExtractor()
        extractor.run(config.path, config.dbExtension, config.imageExtension)
    except Exception as error:
        logger.error(error)

    end_time = gmtime()
    logger.info(f"Ended at {strftime('%Y-%m-%d %H:%M:%S', end_time)}")
    logger.info(f"Running time = {timedelta(seconds= mktime(end_time) - mktime(start_time))}")

if __name__ == '__main__':
    main()