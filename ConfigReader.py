import glob
import sys
import os.path
import configparser

class ConfigReader:
    def __init__(self):
        self._db_extension = None
        self._image_extension = None
        self._path = None

    @property
    def dbExtension(self):
        return self._db_extension
    
    @property
    def imageExtension(self):
        return self._image_extension
    
    @property
    def path(self):
        return self._path

    def run(self):
        if getattr(sys, 'frozen', False):
            cwd = os.path.dirname(sys.executable)
        elif __file__:
            cwd = os.path.dirname(__file__)
        else:
            cwd = "./" # not sure what the case is here
        
        config_path = os.path.join(cwd, "config.ini") 

        config = configparser.ConfigParser()
        if not glob.glob(config_path):
            raise FileNotFoundError(f"Config file [{config_path}] not found!")
        else:
            config.read(config_path)

        try:
            self._db_extension = config['DEFAULT']["db_extension"]
            self._image_extension = config['DEFAULT']["image_extension"]
            self._path = config['USER']["path"]
        except:
            raise KeyError(f"[fail] Error reading config file [{config_path}]! Program aborted")
