import logging
from logging.handlers import RotatingFileHandler
import pathlib


logger = logging.getLogger('ales')
_full_format = '%(asctime)s||%(levelname)s||(%(threadName)s->%(pathname)s->%(funcName)s->%(lineno)d): %(message)s'
full_formatter = logging.Formatter(_full_format)
_short_format = '\n%(asctime)s|| %(levelname)s||(%(threadName)s->%(filename)s->%(funcName)s->%(lineno)d):\n* '\
                '%(message)s'
short_formatter = logging.Formatter(_short_format)
_http_format = '[ %(asctime)s %(levelname)s ] %(message)s'
http_formatter = logging.Formatter(_http_format, datefmt='%d.%m.%Y %H:%M:%S')

# Set up the console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(short_formatter)
logger.addHandler(consoleHandler)

# Set up the file handler
_log_file_path = pathlib.Path(__file__).parent.joinpath('ales.log')
fileHandler = RotatingFileHandler(_log_file_path, maxBytes=2*1024*1024, backupCount=100, encoding="utf-8")
fileHandler.setFormatter(full_formatter)
logger.addHandler(fileHandler)

# Set up logging levels
consoleHandler.setLevel(logging.INFO)
fileHandler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
