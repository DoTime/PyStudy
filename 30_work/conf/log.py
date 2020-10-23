import logging
import logging.config
import yaml
import os
import threading

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'log.yml'), 'r') as _log_:
    dict = yaml.load(_log_,Loader=yaml.FullLoader)
    logging.config.dictConfig(dict)

logger = logging.getLogger()

fileLoggers={}
lock = threading.RLock()

def getFileLogger(name,log_dir=None):
    with lock:
        global fileLoggers
        if(not name in fileLoggers):
            formatter = logging.Formatter(dict['formatters']['simple']['format'])

            path=name+".log"
            if(log_dir!=None):
                os.makedirs(log_dir,exist_ok=True)
                path=os.path.join(log_dir,path)

            handler = logging.FileHandler(path, mode='a')
            handler.setLevel(dict['root']['level'])
            handler.setFormatter(formatter)

            logger = logging.getLogger(name)
            logger.setLevel(dict['root']['level'])
            logger.addHandler(handler)
            fileLoggers[name]=logger
        pass
    return fileLoggers[name]


if __name__=="__main__":
    logger = logging.getLogger('simpleExample')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

    logger = logging.getLogger()  #默认取root
    logging.info("aaaaa")

    logs=getFileLogger('test')
    logs.info("start func111")