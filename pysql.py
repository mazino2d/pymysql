import os
from typing import Sequence, AnyStr, Any, Callable
from error import PySQLError
import configparser
import logging as logger
import pymysql.cursors as cursors
from pymysqlpool.pool import Pool


class PySQL:
    def __init__(self, conf_tag: str, conf_file='config.ini'):
        super().__init__()
        parser = configparser.ConfigParser()

        if os.path.isfile(conf_file):
            parser.read(conf_file)
        else:
            raise FileNotFoundError()

        config = parser[conf_tag]

        username = config['username']
        password = config['password']
        host = config['host']
        port = int(config['port'])
        schema = config['schema']

        try:
            min_size = int(config['minConnection'])
            max_size = int(config['maxConnection'])
        except:
            min_size = 0
            max_size = 10

        self._pool = Pool(user=username, password=password, host=host, port=port,
                          db=schema, min_size=min_size, max_size=max_size, autocommit=True)

    def excute(self, query: AnyStr, param: Sequence[Any] = (),
               func: Callable = lambda row: row) -> int:

        try:
            conn = self._pool.get_conn()
            try:
                with conn.cursor() as cursor:
                    count: int = cursor.execute(query, param)
                    rows = cursor.fetchall()
                    for row in rows:
                        func(row)
            except Exception as e:
                count = PySQLError.PUT_MYSQL_FAIL
                logger.error(e)
        except Exception as e:
            count = PySQLError.UNKNOWN_ERROR
            logger.error(e)

        return count
