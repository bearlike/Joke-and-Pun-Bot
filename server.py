#!/usr/bin/env python3

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv

import warnings
warnings.filterwarnings("ignore")

load_dotenv()

# logging.basicConfig(filename='joker_chat.log',
#                     format='%(asctime)s %(levelname)-8s %(message)s',
#                     datefmt='%d-%m-%Y %H:%M:%S',
#                     level=logging.WARNING)


def init_app():
    from Api.api import app
    app.run(host=os.environ.get("BIND_HOST", '0.0.0.0'),
            port=os.environ.get("PORT", 5000),
            debug=bool(strtobool(os.getenv('DEBUG', 'False'))),
            use_reloader=True)


if __name__ == "__main__":
    print("Server started...")
    init_app()
