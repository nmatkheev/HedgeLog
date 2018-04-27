import logging
import logging.config

from actor import ActorLog
from multiprocessing import Process
from logging.handlers import DEFAULT_TCP_LOGGING_PORT

sample_config = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'simple': {
                'format': '%(levelname)s,%(asctime)s,%(message)s',
                'datefmt': '%d/%m/%Y %H:%M:%S'
            },
        },
        'handlers': {
            'mogol_h': {
                'level': 'INFO',
                'class': 'logging.handlers.SocketHandler',
                'host': '127.0.0.1',
                'port': DEFAULT_TCP_LOGGING_PORT,
                'formatter': 'simple'
            },
            'piston_h': {
                'level': 'INFO',
                'class': 'logging.handlers.SocketHandler',
                'host': '127.0.0.1',
                'port': DEFAULT_TCP_LOGGING_PORT,
                'formatter': 'simple'
            },
        },
        'loggers': {
            'mogol': {
                'handlers': ['mogol_h'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'piston': {
                'handlers': ['piston_h'],
                'level': 'INFO',
                'propagate': False
            },
        }
    }


logging.config.dictConfig(sample_config)

def proc1():
    act1 = ActorLog('mogol')
    act1.lesopoval('bugor')

def proc2():
    act2 = ActorLog('piston')
    act2.lesopoval('atyatya')


if __name__ == '__main__':
    # fd_to_search = ['mogol', 'piston']
    # fds = []
    # ldict = logging.Logger.manager.loggerDict
    # for k, val in logging.Logger.manager.loggerDict.items():
    #     if k in fd_to_search and val.hasHandlers():
    #         fds.extend([fd.stream.fileno() for fd in val.handlers])

    p_list = [
              Process(target=proc1),
              Process(target=proc2)
    ]
    # p_list = [Process(target=proc1)]
    for p in p_list:
        p.start()

    for p in p_list:
        p.join()
