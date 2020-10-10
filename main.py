from loguru import logger
from tqdm import tqdm
from argparse import ArgumentParser
import argparse


def run_parser():
    """
    Setup argsparse to include all arguments required for an unzip utility.
    Please add args as you implement functionality
    """
    parser = argparse.ArgumentParser(description="unzip utility")
    parser.add_argument("-q", "--quiet", action="store_true")
    return parser.parse_args()


def main():
    """
    main: the main method, which parses the args from command line and runs the program as requested
    """
    args = run_parser()
    if args.quiet:
        logger.disable(__name__)
    # Other argsparse logic


if __name__ == "__main__":
    main()
