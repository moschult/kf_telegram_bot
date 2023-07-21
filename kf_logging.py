import argparse

import logging


def start_logging():
    parser = argparse.ArgumentParser(description='Create Configuration')
    parser.add_argument('--log', type=str, help='Loglevel',
                        default="WARNING")

    args = parser.parse_args()
    getattr(logging, args.log.upper())
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log)
    logging.basicConfig(level=numeric_level)
    logging.info("Starting application")
