import sys, traceback
import argparse
import logging
import os.path
from timeit import default_timer as timer

# logging
logger= logging.getLogger('runtime')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler('runtime.log')
logger.addHandler(ch)
logger.addHandler(fh)


def run_project(args):
    logger.info("Staring analysis on input_file %s" % args.load_file)
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug Mode")
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Starting project:')
    parser.add_argument('--load_file', help='The csv file to load from',
                        default='dataset/mini.csv')
    parser.add_argument('--out_file', help='The csv file for analysis',
                        default='dataset/analysis.csv')
    parser.add_argument('--limit', help='Limit the number of records to load (use only for testing)', type=int, dest='limit', default=None)
    parser.add_argument('--debug', action='store_true',
                        help='Run in debug mode')

    args = parser.parse_args()
    run_project(args)