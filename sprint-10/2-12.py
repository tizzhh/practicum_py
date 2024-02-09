# example_for_log.py

import logging

from logging.handlers import RotatingFileHandler


logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s',
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    'my_logger.log', maxBytes=50000000, backupCount=5
)
logger.addHandler(handler)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

logger.debug('123')  # Когда нужна отладочная информация
logger.info('Сообщение отправлено')  # Когда нужна дополнительная информация
logger.warning('Большая нагрузка!')  # Когда что-то идёт не так, но работает
logger.error('Бот не смог отправить сообщение')  # Когда что-то сломалось
logger.critical('Всё упало! Зовите админа!1!111')  # Когда всё совсем плохо

try:
    42 / 0
except Exception as e:
    logger.exception('Cannot divide by zero')
