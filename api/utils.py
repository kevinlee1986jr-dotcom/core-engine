import logging

class Utilities:
    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)

    @staticmethod
    def setup_logger():
        logger = get_logger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def get_datetime():
        import datetime
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_random_string(length):
        import random
        import string
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    @staticmethod
    def convert_to_dict(value):
        if isinstance(value, dict):
            return value
        try:
            return value.__dict__
        except AttributeError:
            return {str(key): value for key, value in vars(value).items()}

    @staticmethod
    def is_list(value):
        return isinstance(value, list)