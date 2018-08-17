from logging import basicConfig, getLogger, DEBUG

def get_logger(module_name):
    FORMAT = '%(asctime)-15s %(name)s %(message)s'
    basicConfig(level=DEBUG, format=FORMAT)
    logger = getLogger(module_name)

    return logger
