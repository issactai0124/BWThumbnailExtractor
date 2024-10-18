import logging
from time import localtime, strftime, mktime
from datetime import timedelta

start_time = localtime()

ver = "1.0"
logger = logging.getLogger()
logfile = f"bwExtract_v{ver}_{strftime('%Y%m%d%H%M%S', start_time)}.log"
format = '%(message)s'
handlers = [logging.FileHandler(logfile), logging.StreamHandler()]
logging.basicConfig(level=logging.INFO, format=format, handlers=handlers)

def printCurrentTime():
    return f"[{strftime('%Y-%m-%d %H:%M:%S %z', localtime())}]"

def start():
    logger.info(f"{printCurrentTime()} BW Thumbnail Extractor ver{ver} started")

def info(text):
    logger.info(f"{printCurrentTime()} {text}")

def warning(text):
    logger.warning(f"{printCurrentTime()} {text}")

def error(text):
    logger.error(f"{printCurrentTime()} {text}")

def finish():
    end_time = localtime()
    logger.info(f"{printCurrentTime()} BW Thumbnail Extractor ver{ver} ran successfully")
    logger.info(f"{printCurrentTime()} Running time = {timedelta(seconds= mktime(end_time) - mktime(start_time))}")