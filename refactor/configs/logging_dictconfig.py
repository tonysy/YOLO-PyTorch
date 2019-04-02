import logging
from logging.config import dictConfig

logging_config = dict(
    version = 1,
    formatters = {
        'f_t': {'format':
                   '\n %(asctime)s | %(levelname)s | %(name)s \t %(message)s'}

    },
    handlers = {
        'stream_handler':{
            'class': 'logging.StreamHandler',
            'formatter': 'f_t',
            'level': logging.INFO},
        # 'file_handler':{
        #     'class': 'logging.FileHandler',
        #     'formatter': 'f_t',
        #     'level': logging.INFO,
        #     'filename': None,
        # }
    },
    root = {
        'handlers': ['stream_handler'],#, 'file_handler'],
        'level': logging.DEBUG,
    },
)

def create_logger():
    dictConfig(logging_config)
    logger = logging.getLogger()
    return logger