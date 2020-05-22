import requests
from merry import Merry
from requests import ConnectTimeout, ConnectionError
import logging

logging.basicConfig(
    format=
    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO)

merry = Merry()
merry.logger.disabled = True
catch = merry._try


class BaseClass(object):
    @staticmethod
    @merry._except(ZeroDivisionError)
    def process_zero_division_error(e):
        logging.error('zero_division_error ' + e)

    @staticmethod
    @merry._except(FileNotFoundError)
    def process_file_not_found_error(e):
        logging.error('file_not_found_error '+ e)

    @staticmethod
    @merry._except(ConnectionError)
    def process_connect_timeout(e):
        logging.error('connect_timeout ' + e)

    @staticmethod
    @merry._except(Exception)
    def process_exception(e):
        logging.error('exception type:' +  type(e) + e)
