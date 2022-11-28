from args import request as requestCommand
from commands import make_request

import argparse


def main():
    parser = argparse.ArgumentParser()

    # Arguments
    parser.add_argument(
        requestCommand["shortCommand"], requestCommand["longCommand"], help=requestCommand["help"], nargs=2,
        dest="request")

    parser.add_argument("-v", help="Make a verbose script", type=bool, default=False, metavar="--verbose", dest="verbose")

    args_parse = parser.parse_args()


    if args_parse.request:
        make_request.main(args_parse)


if __name__ == '__main__':
    main()
