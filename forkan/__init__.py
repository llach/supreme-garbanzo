import os
import errno
import logging
import coloredlogs

from logging.config import dictConfig

weights_path = os.environ['HOME'] + '/.keras/forkan/weights/'
dataset_path = os.environ['HOME'] + '/.keras/datasets/'
log_file = os.environ['HOME'] + '/.keras/forkan/log.txt'

logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '%(asctime)s [%(levelname)-2s] %(name)-4s %(message)s',
              'datefmt': '%H:%M'}
        },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root={
        'handlers': ['h'],
        'level': logging.DEBUG,
        },
)

# config for coloredlogs
field_styles = coloredlogs.DEFAULT_FIELD_STYLES
fmt = '%(asctime)s [%(levelname)-8s] %(name)-4s %(message)s'
datefmt = '%H:%M'

# surpress matplotlib debug bloat
logging.getLogger('matplotlib').setLevel(logging.WARNING)

dictConfig(logging_config)
logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG', fmt=fmt, datefmt=datefmt)

for dir in [weights_path, dataset_path]:
    if not os.path.isdir(dir):
        try:
            os.makedirs(dir)
            logger.info('Creating {}'.format(dir))
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(dir):
                pass
