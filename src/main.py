from args import request as requestCommand
from commands import make_request

import argparse


def main():
    parser = argparse.ArgumentParser()

    # Arguments
    parser.add_argument(
        requestCommand["shortCommand"], requestCommand["longCommand"], help=requestCommand["help"], nargs='+')

    parser.add_argument("-u", "--url", nargs='+', help="Url to make request")

    parser.add_argument("-v", "--verbose", help="Make a verbose script")

    args_parse = parser.parse_args()

    

    if args_parse.request:
        make_request.main(args_parse)


if __name__ == '__main__':
    main()
