import logging
import sys
from core_engine.config import Config
from core_engine.app import App

def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    config = Config()
    app = App(config)
    app.run()

if __name__ == '__main__':
    sys.exit(main())